import base64
import json
import boto3
from datetime import datetime

print('Loading function')

s3_client = boto3.client("s3")

# Converting datetime object to string
dateTimeObj = datetime.now()

# format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")

# List for the records
kinesisRecords = []

def lambda_handler(event, context):
    
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        
        # append each record to a list
        kinesisRecords.append(payload)
        
        # for logging
        #print("Decoded payload: "+ payload)
    
    # make a string out of the list, backslash n for new line in the s3 file
    ex_string = '\n'.join(kinesisRecords)
    
    # generate the name for the file with the timestamp
    mykey = 'output-' + timestampStr + '.txt'
    
    # put the file into the s3 bucket
    response = s3_client.put_object(Body=ex_string, Bucket="aws-de-project-bucket", Key=mykey)
    
    return "Successfully processed {} records.".format(len(event['Records']))
