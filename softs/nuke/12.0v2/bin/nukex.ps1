if (!(Test-Path Variable:PSScriptRoot)) { $PSScriptRoot = Split-Path $MyInvocation.MyCommand.Path -Parent }
$nuke_app = "Nuke$env:NUKE_LOCATION_VERSION"
$nukex = '--nukex'
if($myinvocation.expectingInput) { $input | & $nuke_app $nukex @args } else { & $nuke_app $nukex @args }
