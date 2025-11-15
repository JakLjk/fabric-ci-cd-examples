from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items
import argparse


parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('--WorkspaceId', type=str)
parser.add_argument('--Environment', type=str)
parser.add_argument('--RepositoryDirectory', type=str)
parser.add_argument('--ItemsInScope', type=str)
args = parser.parse_args()


allitems = args.ItemsInCope
item_type_in_scope = allitems.split(",")
print(f"Items in scope: {str(item_type_in_scope)}")

target_workspace = FabricWorkspace(
    workspace_id=args.WorkspaceId,
    environment=args.Environment,
    repository_directory=args.RepositoryDirectory,
    item_type_in_scope=item_type_in_scope
)

publish_all_items(target_workspace)

unpublish_all_orphan_items(target_workspace)