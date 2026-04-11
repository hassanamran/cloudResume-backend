import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    
    response = table.get_item(Key={'id': 'visitors'})
    
    if 'Item' not in response:
        count = 1
    else:
        count = int(response['Item']['count']) + 1
    
    table.put_item(Item={'id': 'visitors', 'count': count})
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'count': count
        })
    }