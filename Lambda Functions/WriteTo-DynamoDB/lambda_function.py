import base64
import json
import boto3
from datetime import datetime

print('Loading function')

client = boto3.client("dynamodb")

def lambda_handler(event, context):
    num_records = len(event['Records'])
    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
    
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("PAYLOAD:", payload)

        # transform the json string into a dictionary
        dict_record = json.loads(payload)
        dict_record = json.loads(dict_record)
        print("DICT_RECORD", dict_record)
        print("NEW TYPE:", type(dict_record))
        
        #tmp_dict = json.loads(dict_record)
        
        #############################################
        # Create Customer Row
        # TO DO - enter some sort of error handling to ensure that the value is not NULL or 'NA'
        # not sure what a default would be, perhaps some preprocessing would have to occur int he python script to only
        # send items that are valid and drop anything missing
        if dict_record['CustomerID'] is None:
            continue
        else:
            customer_key = {"CustomerID": {"N": str(dict_record["CustomerID"])} }
            print("Customer Key:", customer_key)
            
            ex_customer = {str(dict_record['InvoiceNo']): {'Value': {'S':'Dummy Text'}, 'Action': 'PUT'}}
            print("Ex_Customer Attributes:", ex_customer)
            
            response = client.update_item(TableName='Customers', Key=customer_key, AttributeUpdates=ex_customer)
        
        #############################################
        # Create Inventory Row
        inventory_key = dict()
        inventory_key.update({"InvoiceNo": {"S": str(dict_record['InvoiceNo'])}})
        
        # create export dictionary
        ex_dynamoRecord = dict()
        
        # remove invoice and stock code from dynamoDB record
        stock_dict = dict_record.copy()
        stock_dict.pop('InvoiceNo', None)
        stock_dict.pop('StockCode', None)
        
        # turn the dict into a json
        stock_json = json.dumps(stock_dict)
        
        # create a record for the InvoiceNo as the key
        # add the stock json to the column with the name of the stock number
        ex_dynamoRecord.update({str(dict_record['StockCode']): {"Value": {"S": stock_json}, "Action": "PUT"}})
        
        # debugging
        print(ex_dynamoRecord)
        
        response = client.update_item(TableName='Invoices', Key=inventory_key, AttributeUpdates=ex_dynamoRecord)
        
    return "Successfully processed {} records".format(len(event['Records']))