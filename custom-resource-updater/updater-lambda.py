import re
import uuid

def iterate(Resources, resource_list):
    if not resource_list:
        for Resource in Resources:
            if re.match(Resources[Resource]["Type"], "Custom:*") or Resources[Resource]["Type"] == "AWS::CloudFormation::CustomResource":
                Resources[Resource]["Properties"]["DummyProperty"] = str(uuid.uuid4())
    else:
        for Resource in Resources:
            if Resource in resource_list and re.match(Resources[Resource]["Type"], "Custom:*") or Resources[Resource]["Type"] == "AWS::CloudFormation::CustomResource":
                Resources[Resource]["Properties"]["DummyProperty"] = str(uuid.uuid4())
def lambda_handler(event, context):
    stack_template = event["fragment"]
    resource_list = []
    if "ResourcesToUpdate" in stack_template:
        resource_list = stack_template["ResourcesToUpdate"]
        stack_template.pop("ResourcesToUpdate")
    iterate(stack_template["Resources"], resource_list)

    macro_response = {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": stack_template
    }
    return macro_response
