import json
import boto3
import os
from datetime import datetime


ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ALERTS_TABLE']) 

#Trigger Keywords
ALERT_KEYWORDS = ["ERROR", "CRITICAL", "FAILURE"]

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        log_level = body.get('level', '').upper()
        message = body.get('message', '')
        email = body.get('customerEmail')
        service = body.get('service', 'Unknown Service')
        timestamp = body.get('timestamp', datetime.utcnow().isoformat())
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }