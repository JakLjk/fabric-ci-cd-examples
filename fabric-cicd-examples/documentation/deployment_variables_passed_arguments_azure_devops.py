'''Leverages Default Credential Flow for authentication. Accepts parameters passed into Python during execution.'''

import sys
import os
from pathlib import Path

from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items, change_log_level

# Force unbuffered output like `python -u`
sys.stdout.reconfigure(line_buffering=True, write_through=True)
sys.stderr.reconfigure(line_buffering=True, write_through=True)

# Enable debugging if defined in Azure DevOps pipeline
if os.getenv("SYSTEM_DEBUG", "false").lower() == "true":
    change_log_level("DEBUG")

# Accept parsed arguments
parser = argparse.ArgumentParser(description='Process Azure Pipeline arguments.')
parser.add_argument('--workspace_id', type=str)
parser.add_argument('--environment', type=str)
parser.add_argument('--repository_directory', type=str)
parser.add_argument('--items_in_scope', type=str)
args = parser.parse_args()

# Sample values for FabricWorkspace parameters
workspace_id = args.workspace_id
environment = args.environment
repository_directory = args.repository_directory
item_type_in_scope = args.items_in_scope.split(",")

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