import json
import boto3

def lambda_handler(event, context):

    print("MyEvent:")
    print(event)
    
    method = event["httpMethod"]
    
    if method == "GET":
        dynamo_client = boto3.client('dynamodb')
        
        im_invoiceID = event['queryStringParameters']['InvoiceNo']
        response = dynamo_client.get_item(TableName = 'Invoices', Key = {'InvoiceNo':{'S': str(im_invoiceID)}})
        print(response['Item'])

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == "POST":
        p_record = event['body']
        recordstring = json.dumps(p_record)

        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIDataStream',
            Data= recordstring,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
        
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
    

