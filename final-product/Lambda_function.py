import json
import boto3
import os

endpoint_name = "jumpstart-dft-meta-textgeneration-llama-2-7b-f"
runtime = boto3.client("sagemaker-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    
    payload = json.loads(json.dumps(event))

    #invoke endpoint
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=json.dumps(payload),
        CustomAttributes="accept_eula=true",
    )

    result = json.loads(response["Body"].read().decode("utf8"))
    pred = result[0]['generation']['content']
    
    return pred