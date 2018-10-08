<h3> Dynamic DynamoDB Mapping </h3>

Add Key-Pairs from your DynamoDB to CloudFormation Mappings section

<h3> Basic Usage </h3>

Specify the <code>TableName</code> and the <code>AttributeValues</code> that you wish to include as a separate section under the title <code>DynamoDBMapper</code>. Within the <code>Mappings</code> section, specify the Key Name in the format <code>dynamo-db=KEY-NAME</code>, so that the Macro replaces the section with the Key-Value pairs.

<h3> Available Options </h3>

<h4> Supports Sort Keys </h4>

You can specify the composite primary keys as follows : <code>dynamo-db=PARTITION_KEY,SORT_KEY</code> and the Macro would replace the term by the item from the DynamoDB table.

<h4> Currently Supported Item types </h4>

<ul>
  <li> String </li>
  <li> Integer </li>
  <li> List </li>
</ul>

<h3> Author </h3>

Roshan Arvind Sivakumar

Cloud Support Associate<br>
Amazon Web Services
