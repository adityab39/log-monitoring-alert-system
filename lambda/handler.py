import json
import boto3
import os
from datetime import datetime


ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ALERTS_TABLE']) 
