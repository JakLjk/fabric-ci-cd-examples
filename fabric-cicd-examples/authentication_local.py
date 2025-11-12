'''Log in with Azure CLI (az login) or Azure PowerShell (Connect-AzAccount) prior to execution'''

from pathlib import Path

from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent.parent

# Sample values for FabricWorkspace parameters
workspace_id = "9039a6e2-f2ca-4cfd-9692-daadbec4946c"
environment = "TEST"
repository_directory = str(root_directory / "your-workspace-directory")
item_type_in_scope = ["Notebook", "DataPipeline", "Environment"]

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)