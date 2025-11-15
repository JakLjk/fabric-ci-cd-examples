'''
Log in with Azure CLI (az login) prior to execution
OR (Preferred) Use Az CLI ADO Tasks with a Service Connection
'''

import sys
import os
from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items, change_log_level

# Force unbuffered output like `python -u`
sys.stdout.reconfigure(line_buffering=True, write_through=True)
sys.stderr.reconfigure(line_buffering=True, write_through=True)

# Enable debugging if defined in Azure DevOps pipeline
if os.getenv("SYSTEM_DEBUG", "false").lower() == "true":
    change_log_level("DEBUG")

# Assumes your script is one level down from root
root_directory = Path(__file__).resolve().parent

# Sample values for FabricWorkspace parameters
workspace_id = "your-workspace-id"
environment = "your-environment"
repository_directory = str(root_directory / "your-workspace-directory")
item_type_in_scope = ["Notebook", "DataPipeline", "Environment"]

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