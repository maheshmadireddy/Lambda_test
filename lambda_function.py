# This is a python based AWS Lambda
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda via CodePipeline!'
    }
