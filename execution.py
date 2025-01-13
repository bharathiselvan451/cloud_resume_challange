import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    dyanmodb = boto3.resource('dynamodb')
    table = dyanmodb.Table('resumedb')
    value = table.get_item(Key={'key': 'key'})
    print("current value is ......")
    print(value['Item']['count'])
    table.put_item(Item={'key': 'key', 'count': value['Item']['count'] + 1})

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': int(value['Item']['count'])
    }
