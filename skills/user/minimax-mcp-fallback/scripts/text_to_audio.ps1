# minimax-mcp-fallback :: text_to_audio.ps1
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Text,
    [string]$VoiceId = "male-qn-qingse",
    [ValidateSet("speech-01","speech-02","speech-2.6-hd","speech-2.6-turbo")] [string]$Model = "speech-01",
    [ValidateRange(0.5,2.0)] [double]$Speed = 1.0,
    [ValidateRange(0,10)]    [double]$Vol   = 1.0,
    [int]$Pitch = 0,
    [ValidateSet("happy","sad","angry","fearful","disgusted","surprised","neutral")] [string]$Emotion = "happy",
    [int]$SampleRate = 32000,
    [int]$Bitrate    = 128000,
    [int]$Channel    = 1,
    [ValidateSet("pcm","mp3","flac")] [string]$Format = "mp3",
    [string]$LanguageBoost = "auto",
    [string]$ApiKey,
    [string]$ApiHost = "https://api.minimaxi.com",
    [string]$OutFile = (Join-Path $env:USERPROFILE "Desktop\minimax-fallback" ("tts_{0}.mp3" -f (Get-Date -Format "yyyyMMdd_HHmmss")))
)
. (Join-Path $PSScriptRoot "_env.ps1") -ApiKey $ApiKey -ApiHost $ApiHost
. (Join-Path $PSScriptRoot "_http.ps1")

$body = @{
    model           = $Model
    text            = $Text
    voice_setting   = @{
        voice_id = $VoiceId
        speed    = $Speed
        vol      = $Vol
        pitch    = $Pitch
        emotion  = $Emotion
    }
    audio_setting   = @{
        sample_rate = $SampleRate
        bitrate     = $Bitrate
        channel     = $Channel
        format      = $Format
    }
    language_boost  = $LanguageBoost
}
$bytes = Invoke-MiniMaxApi -Path "/v1/text_to_speech" -Body $body -ReturnBytes
$path  = Save-MiniMaxMedia -Bytes $bytes -OutFile $OutFile
Write-Output $path
