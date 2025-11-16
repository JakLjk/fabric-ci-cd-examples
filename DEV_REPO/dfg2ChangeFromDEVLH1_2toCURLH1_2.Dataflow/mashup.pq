[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "dataFromDataflow_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared dataFromDataflow = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "0b757bbc-b963-4071-9c9e-b2799e4ba796"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "59c7187a-f6a9-4486-b4d6-740b0dab5028"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "dataFromDataflow"]}[Content],
  #"Navigation 4" = #"Navigation 3"{[Name = "bikesUpload.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 4", [Delimiter = ",", Columns = 13, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"day", Int64.Type}, {"mnth", Int64.Type}, {"year", Int64.Type}, {"season", Int64.Type}, {"holiday", Int64.Type}, {"weekday", Int64.Type}, {"workingday", Int64.Type}, {"weathersit", Int64.Type}, {"temp", type number}, {"atemp", type number}, {"hum", type number}, {"windspeed", type number}, {"rentals", Int64.Type}})
in
  #"Changed column type";
shared dataFromDataflow_DataDestination = let
  Pattern = Lakehouse.Contents([HierarchicalNavigation = null, CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "0b757bbc-b963-4071-9c9e-b2799e4ba796"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "805ae812-074e-4090-bbba-d25165fa8964"]}[Data],
  TableNavigation = Navigation_2{[Id = "bikesFromDataflowLH2", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
