'''Pass the required SPN values directly into the credential object, does not require AZ PowerShell or AZ CLI'''

from pathlib import Path

from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent

# Sample values for FabricWorkspace parameters
workspace_id = "your-workspace-id"
environment = "your-environment"
repository_directory = str(root_directory / "your-workspace-directory")
item_type_in_scope = ["Notebook", "DataPipeline", "Environment"]

# Use Azure CLI credential to authenticate
client_id = "your-client-id"
client_secret = "your-client-secret"
tenant_id = "your-tenant-id"
token_credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

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