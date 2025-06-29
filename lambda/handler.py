import json
import boto3
import os
from datetime import datetime
import uuid


ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ALERTS_TABLE'])

ALERT_KEYWORDS = ["ERROR", "CRITICAL", "FAILURE"]

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        body = event.get('body')
        if body:
            body = json.loads(body)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing body'})
            }

        log_level = body.get('log_level', '').upper()
        message = body.get('message', '')
        email = body.get('email')
        service = body.get('service', 'Unknown Service')
        timestamp = body.get('timestamp', datetime.utcnow().isoformat())

        if any(keyword in log_level or keyword in message.upper() for keyword in ALERT_KEYWORDS):
            ses.send_email(
                Source=os.environ['ALERT_EMAIL_FROM'],
                Destination={'ToAddresses': [email]},
                Message={
                    'Subject': {'Data': f' Alert from {service}'},
                    'Body': {'Text': {'Data': f'{log_level} detected: {message}\nTimestamp: {timestamp}'}}
                }
            )

            response = table.put_item(Item={
                'id': str(uuid.uuid4()),
                'email': email,
                'service': service,
                'log_level': log_level,
                'message': message,
                'timestamp': timestamp
            })


        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Processed'})
        }

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }