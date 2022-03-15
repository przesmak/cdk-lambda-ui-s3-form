import json, os, io
import boto3
from botocore.exceptions import ClientError

bucket_name = os.environ['S3_BUCKET_NAME']

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    s3_client = boto3.client('s3')

    if event['httpMethod'] == 'POST':
        try: 
            s3_client.upload_fileobj(io.BytesIO(json.dumps(event['body']).encode()), bucket_name, "{}.json".format(event['path']))
        except ClientError as error: 
            print("Client error in uploading a file {}".format(error))

    if event['httpMethod'] == 'GET':
        try: 
            temp_file = "/tmp/{}.json".format(event['path'])
            s3_client.download_file(bucket_name, "{}.json".format(event['path']), temp_file)
            with open(temp_file, 'r', encoding='UTF-8') as f: 
                print(f.read())
        except ClientError as error: 
            print("Client error in downloading a file from the bucket {}".format(error))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT"
        },
        'body': 'Hello from the report. HTTP Method: {} Body: {}\n'.format(json.dumps(event['httpMethod']), json.dumps(event['body']))
    }