[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Query_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "File", TransformationQueryName = "Query_DataDestinationTransform"]]]}]
shared Query = let
  Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/TheKivs/Bike-Rentals/refs/heads/master/bikes.csv"), [Delimiter = ",", Columns = 13, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"hr", Int64.Type}, {"holiday", Int64.Type}, {"workingday", Int64.Type}, {"temp", type number}, {"hum", type number}, {"windspeed", type number}, {"cnt", Int64.Type}, {"instant", Int64.Type}, {"mnth", Int64.Type}, {"yr", Int64.Type}, {"Clear to partly cloudy", Int64.Type}, {"Light Precipitation", Int64.Type}, {"Misty", Int64.Type}})
in
  #"Changed column type";
shared Query_DataDestination = let
  Pattern = Lakehouse.Contents([HierarchicalNavigation = null, CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "0b757bbc-b963-4071-9c9e-b2799e4ba796"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "59c7187a-f6a9-4486-b4d6-740b0dab5028"]}[Data],
  Navigation_3 = Navigation_2{[Id = "Files", ItemKind = "Folder"]}[Data],
  FileNavigation = Navigation_3{[Name = "bikes.csv"]}?[Content]?
in
  FileNavigation;
shared Query_DataDestinationTransform = (binaryStream, columnNameAndTypePairs) => let
  Pattern = Csv.Document(binaryStream, [Columns = List.Transform(columnNameAndTypePairs, each _{0}), CsvStyle = CsvStyle.QuoteAfterDelimiter, IncludeByteOrderMark = true, ExtraValues = ExtraValues.Ignore, Delimiter = ",", Encoding = 65001]),
  PromoteHeaders = Table.PromoteHeaders(Pattern),
  TransformColumnTypes = Table.TransformColumnTypes(PromoteHeaders, columnNameAndTypePairs, [MissingField = MissingField.Ignore])
in
  TransformColumnTypes;
