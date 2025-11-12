# Check exit code in PowerShell
fab get DEV_WORKSPACE.Workspace
if ($LASTEXITCODE -eq 0) {
    Write-Host "Success"
} elseif ($LASTEXITCODE -eq 4) {
    Write-Host "Authentication required"
    fab auth login
} else {
    Write-Host "Command failed with exit code: $LASTEXITCODE"
}