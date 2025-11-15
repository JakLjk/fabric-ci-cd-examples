'''Log in with Azure CLI (az login) prior to execution'''

from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent.parent

# Sample values for FabricWorkspace parameters
workspace_id = "cffea74c-18ab-43ae-b8be-edcf30ced68e"
environment = "TEST"
repository_directory = str(root_directory / "DEV_REPO")
item_type_in_scope = ["Notebook", "DataPipeline", "Environment", "SemanticModel", "Report"]

# Use Azure CLI credential to authenticate
token_credential = AzureCliCredential()

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
    token_credential=token_credential,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)