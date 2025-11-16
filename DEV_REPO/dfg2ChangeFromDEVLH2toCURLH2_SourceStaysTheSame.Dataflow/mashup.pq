[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Trip_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared Trip = let
  Source = Fabric.Warehouse([HierarchicalNavigation = null]),
  #"Navigation 1" = Source{[workspaceId = "d395a6fb-0129-443e-9149-b7d13f9397aa"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[warehouseId = "b54217e1-7e0c-4eb8-9de3-2bec8db6a9a2"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Schema = "dbo", Item = "Trip"]}[Data]
in
  #"Navigation 3";
shared Trip_DataDestination = let
  Pattern = Lakehouse.Contents([HierarchicalNavigation = null, CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "0b757bbc-b963-4071-9c9e-b2799e4ba796"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "805ae812-074e-4090-bbba-d25165fa8964"]}[Data],
  TableNavigation = Navigation_2{[Id = "TripFromSourceWH", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
