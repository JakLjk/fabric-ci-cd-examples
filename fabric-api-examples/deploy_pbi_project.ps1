# The script uses the FabricPS-PBIP module,
# which serves as a wrapper for the Fabric APIs
# and handles tasks such as authentication,
# asynchronous calls, and metadata management
# for Power BI project files.


# Parameters 
$workspaceName = "DEV_WORKSPACE]"
$pbipSemanticModelPath = "C:\Users\jakub\Documents\Learning\CI_CD\fabric_ci_cd\sample_pbi_project\Sales Analysis - Enforce model security.SemanticModel"
$pbipReportPath = "C:\Users\jakub\Documents\Learning\CI_CD\fabric_ci_cd\sample_pbi_project\Sales Analysis - Enforce model security.Report"
$currentPath = (Split-Path $MyInvocation.MyCommand.Definition -Parent)
Set-Location $currentPath

# Download modules and install
New-Item -ItemType Directory -Path ".\modules" -ErrorAction SilentlyContinue | Out-Null
@("https://raw.githubusercontent.com/microsoft/Analysis-Services/master/pbidevmode/fabricps-pbip/FabricPS-PBIP.psm1"
, "https://raw.githubusercontent.com/microsoft/Analysis-Services/master/pbidevmode/fabricps-pbip/FabricPS-PBIP.psd1") |% {
    Invoke-WebRequest -Uri $_ -OutFile ".\modules\$(Split-Path $_ -Leaf)"
}
if(-not (Get-Module Az.Accounts -ListAvailable)) { 
    Install-Module Az.Accounts -Scope CurrentUser -Force
}
Import-Module ".\modules\FabricPS-PBIP" -Force

# Authenticate
Set-FabricAuthToken -reset

# Ensure workspace exists
$workspaceId = New-FabricWorkspace  -name $workspaceName -skipErrorIfExists

# Import the semantic model and save the item id
$semanticModelImport = Import-FabricItem -workspaceId $workspaceId -path $pbipSemanticModelPath

# Import the report and ensure its binded to the previous imported report
$reportImport = Import-FabricItem -workspaceId $workspaceId -path $pbipReportPath -itemProperties @{"semanticModelId" = $semanticModelImport.Id}