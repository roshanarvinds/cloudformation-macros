import re
import boto3

def format_item(item):
    if isinstance(item, dict):
        for k in item:
            if k in ('S', 'N'):
                return item[k]
            elif k == 'L':
                return format_item(item[k])
            else:
                item[k] = format_item(item[k])
    elif isinstance(item, list):
        for i, v in enumerate(item):
            item[i] = format_item(v)
    return item

def return_dynamodb_item(table_name, attributes, key_types):
    client = boto3.client('dynamodb')
    if attributes:
        return client.get_item(
            TableName=table_name,
            Key=key_types,
            ProjectionExpression=attributes
        )
    else:
        return client.get_item(
            TableName=table_name,
            Key=key_types
        )

def iterate(item, params):
    if isinstance(item, dict):
        for k in item:
            item[k] = iterate(item[k], params)
    elif isinstance(item, list):
        for i, v in enumerate(item):
            item[i] = iterate(v, params)
    elif isinstance(item, str):
        if re.match('dynamo-db=*', item):
            key = item.split('=')[1]
            if params["sort_key"]:
                hash_key, range_key = key.split(',')
                params["key_list"].append([hash_key, range_key])
            else:
                params["key_list"].append([key])
    return item


def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    stack_template = event["fragment"]
    table_name = stack_template["DynamoDBMapper"]["TableName"]
    primary_key = ""
    sort_key = ""
    attribute_values = ""
    key_types = {}
    key_list = []
    if "AttributeValues" in stack_template["DynamoDBMapper"]:
        attribute_values = ','.join(
            stack_template["DynamoDBMapper"]["AttributeValues"])
    else:
        attribute_values = None
    try:
        table_description = client.describe_table(TableName=table_name)

    except Exception as e:
        print("Table does not exist!")
        return

    if len(table_description["Table"]["KeySchema"]) == 2:
        sort_key = table_description["Table"]["KeySchema"][1]["AttributeName"]
    primary_key = table_description["Table"]["KeySchema"][0]["AttributeName"]

    table_attributes = table_description["Table"]["AttributeDefinitions"]

    params = {
        "table_name": table_name,
        "primary_key": primary_key,
        "sort_key": sort_key,
        "key_list": key_list
    }

    iterate(stack_template["Mappings"], params)
    for key, mapping in zip(key_list, stack_template["Mappings"]):

        if len(table_attributes) == 1:
            key_types[table_attributes[0]["AttributeName"]] = {table_attributes[0]["AttributeType"]: key[0]}
        else:
            for j, i in zip(key, table_attributes):
                key_types[i["AttributeName"]] = {i["AttributeType"]: j}

        response = return_dynamodb_item(table_name, attribute_values, key_types)
        try:
            element = response["Item"]
        except Exception as e:
            print("Given Key Does Not Exist!")
            return
        map_name = "-".join(key)
        stack_template["Mappings"][mapping] = {map_name : format_item(element)}

    stack_template.pop("DynamoDBMapper")
    macro_response = {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": stack_template
    }
    return macro_response
