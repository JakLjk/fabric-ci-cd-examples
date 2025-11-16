[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Table_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared Table = let
  Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i45WckksSUzLyS9X0lEyBGKP1JycfKVYHYhEQGZBak5mXipQwgiIw/OLclLAkn75JalJ+fnZQEFjmC4FhHRwam5iXklmsm9+SmoOUN4EiMFsBVTzoRabArGLG0x/LAA=", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Item = _t, Id = _t, Name = _t]),
  #"Changed column type" = Table.TransformColumnTypes(Source, {{"Item", type text}, {"Id", Int64.Type}, {"Name", type text}}),
  #"Added custom" = Table.TransformColumnTypes(Table.AddColumn(#"Changed column type", "IsDataflow", each if [Item] = "Dataflow" then true else false), {{"IsDataflow", type logical}}),
  #"Added custom 1" = Table.TransformColumnTypes(Table.AddColumn(#"Added custom", "ContainsHello", each if Text.Contains([Name], "Hello") then 1 else 0), {{"ContainsHello", Int64.Type}})
in
  #"Added custom 1";
shared Table_DataDestination = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "e6a8c59f-4b27-48d1-ae03-7f92b1c6458d"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "3d72f90e-61b5-42a8-9c7e-b085d4e31fa2"]}[Data],
  TableNavigation = Navigation_2{[Id = "Items", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;





{
    "formatVersion": "202502",
    "computeEngineSettings": {},
    "name": "Sample Dataflow",
    "queryGroups": [],
    "documentLocale": "en-US",
    "queriesMetadata": {
        "Table": {
            "queryId": "ba67667b-14c0-4536-a92d-feafc73baa4b",
            "queryName": "Table",
            "loadEnabled": false
        },
        "Table_DataDestination": {
            "queryId": "a157a378-b510-4d95-bb82-5a7c80df8b4c",
            "queryName": "Table_DataDestination",
            "isHidden": true,
            "loadEnabled": false
        }
    },
    "connections": [
        {
            "path": "Lakehouse",
            "kind": "Lakehouse",
            "connectionId": "{\"ClusterId\":\"8e4f92a7-3c18-49d5-b6d0-7f2e591ca4e8\",\"DatasourceId\":\"d12c5f7b-90a3-47e6-8d2c-3fb59e01d47a\"}"
        }
    ]
}