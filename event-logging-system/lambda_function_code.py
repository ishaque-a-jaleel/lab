import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'EventLogs'  # DynamoDb table name
table = dynamodb.Table(table_name)

def validate_payload(payload):
    """Validates that the payload contains the required fields."""
    required_fields = ['EventID', 'Timestamp', 'Details']
    for field in required_fields:
        if field not in payload:
            return False, f"Missing required field: {field}"
    return True, "Validation successful"

def lambda_handler(event, context):
    """Lambda function to process log and insert into DynamoDB."""
    try:
        # Handle payload depending on its source
        if 'body' in event:
            # API Gateway scenario: Body is a string
            payload = json.loads(event['body'])
        else:
            # Direct Lambda invocation: event is already a JSON object
            payload = event

        # Validate the payload
        is_valid, message = validate_payload(payload)
        if not is_valid:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": message})
            }

        # Insert the log into DynamoDB
        table.put_item(Item=payload)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Log successfully inserted."})
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format"})
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"DynamoDB error: {e.response['Error']['Message']}"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Unexpected error: {str(e)}"})
        }
    



"""
swap the values of the variables without using additional variables
a=1
b=2

a=a+b
b=a-b  a+b-b
a=a-b  a+b-a
"""

