<#
.SYNOPSIS
Shared helpers for the MiniMax_web_search skill scripts.
.NOTES
Dot-source this file:  . "$PSScriptRoot\_lib.ps1"
#>

function Get-MiniMaxKey {
    $k = [System.Environment]::GetEnvironmentVariable("MINIMAX_API_KEY", "User")
    if (-not $k) { $k = [System.Environment]::GetEnvironmentVariable("MINIMAX_API_KEY", "Process") }
    if (-not $k) {
        Write-Error "MINIMAX_API_KEY is not set. Add it to your User environment variables." -ErrorAction Stop
    }
    return $k
}

function Get-MiniMaxHost {
    $h = [System.Environment]::GetEnvironmentVariable("MINIMAX_API_HOST", "User")
    if (-not $h) { $h = [System.Environment]::GetEnvironmentVariable("MINIMAX_API_HOST", "Process") }
    if (-not $h) { $h = "https://api.minimaxi.com" }
    return $h
}

function Invoke-MiniMaxMcp {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)] [string[]] $PayloadLines,
        [int] $TimeoutSec = 60
    )

    $key = Get-MiniMaxKey
    $env:MINIMAX_API_KEY = $key
    $env:MINIMAX_API_HOST = Get-MiniMaxHost

    $uvx = (Get-Command uvx).Source
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $uvx
    $psi.Arguments = "--from minimax-coding-plan-mcp minimax-coding-plan-mcp -y"
    $psi.RedirectStandardInput  = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError  = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow  = $true
    # 强制子进程输出按 UTF-8 解码
    $psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
    $psi.StandardErrorEncoding  = [System.Text.Encoding]::UTF8

    $proc = [System.Diagnostics.Process]::Start($psi)
    try {
        $payload = ($PayloadLines -join "`n") + "`n"
        # 用 UTF-8 显式写入 stdio，避免 .NET 字符串默认 UTF-16 编码问题
        $utf8 = New-Object System.Text.UTF8Encoding($false)
        $bytes = $utf8.GetBytes($payload)
        $stream = $proc.StandardInput.BaseStream
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Flush()
        $proc.StandardInput.Close()

        $stdOutTask = $proc.StandardOutput.ReadToEndAsync()
        $stdErrTask = $proc.StandardError.ReadToEndAsync()
        $proc.WaitForExit($TimeoutSec * 1000) | Out-Null

        if (-not $proc.HasExited) {
            try { $proc.Kill() } catch {}
            Write-Error "MiniMax MCP server did not exit within $TimeoutSec s" -ErrorAction Stop
        }

        $out = $stdOutTask.Result
        $err = $stdErrTask.Result

        if (($proc.ExitCode -ne 0) -and [string]::IsNullOrWhiteSpace($out)) {
            Write-Error ("MiniMax MCP failed (exit {0}): {1}" -f $proc.ExitCode, $err) -ErrorAction Stop
        }

        # 控制台按 UTF-8 输出，防止中文乱码
        [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        return $out
    } finally {
        if (-not $proc.HasExited) { try { $proc.Kill() } catch {} }
        $proc.Dispose()
    }
}

function Format-MiniMaxSearch {
    param($Result, [switch] $JsonOnly)

    if ($JsonOnly) {
        [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        return $Result
    }

    # 解析最后一条 JSON-RPC 响应
    $last = $null
    foreach ($line in ($Result -split "`n")) {
        $line = $line.Trim()
        if (-not $line.StartsWith("{")) { continue }
        try {
            $obj = $line | ConvertFrom-Json -ErrorAction Stop
            if ($obj.id -and $obj.result) { $last = $obj }
        } catch {}
    }

    if (-not $last) {
        [Console]::Error.WriteLine("[MiniMax] no JSON-RPC response received")
        return $Result
    }

    $content = $last.result.content
    if (-not $content) {
        [Console]::Error.WriteLine("[MiniMax] empty content, raw:")
        [Console]::Error.WriteLine($Result)
        return $Result
    }

    $text = ($content | Where-Object { $_.type -eq "text" } | Select-Object -First 1).text
    if (-not $text) {
        [Console]::Error.WriteLine($Result)
        return $Result
    }

    try {
        $data = $text | ConvertFrom-Json -ErrorAction Stop
    } catch {
        [Console]::Error.WriteLine("[MiniMax] text is not JSON, raw:")
        [Console]::Error.WriteLine($text)
        return $Result
    }

    if ($data.answer) {
        [Console]::Error.WriteLine("# ANSWER")
        [Console]::Error.WriteLine($data.answer)
        [Console]::Error.WriteLine("")
    }

    $i = 0
    foreach ($it in $data.organic) {
        $i++
        [Console]::Error.WriteLine("[$i] $($it.title)")
        [Console]::Error.WriteLine("  url:   $($it.link)")
        if ($it.snippet) {
            $snip = $it.snippet -replace '<[^>]+>', ''
            if ($snip.Length -gt 320) { $snip = $snip.Substring(0,320) + "..." }
            [Console]::Error.WriteLine("  snip:  $snip")
        }
    }

    if ($data.related_searches) {
        [Console]::Error.WriteLine("")
        [Console]::Error.WriteLine("# Related searches:")
        foreach ($rs in $data.related_searches) {
            [Console]::Error.WriteLine("  - $($rs.query)")
        }
    }

    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    return ($data | ConvertTo-Json -Depth 10)
}
