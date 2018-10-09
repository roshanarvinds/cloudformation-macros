import re
import uuid

def iterate(Resources, resource_list=[]):
    for Resource in Resources:
        if re.match(Resource["Type"], "Custom:*") or Resource["Type"] == "AWS::CloudFormation::CustomResource":
            Resource["Properties"]["DummyProperty"] = str(uuid.uuid4())
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    stack_template = event["fragment"]
    resource_list = []
    if "ResourcesToUpdate" in stack_template:
        resource_list = stack_template["ResourcesToUpdate"]
        iterate(stack_template["Resources"], resource_list)
    else:
        iterate(stack_template["Resources"])

    macro_response = {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": stack_template
    }
    return macro_response
