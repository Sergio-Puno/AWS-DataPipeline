import json
import boto3
import base64

output = []

def lambda_handler(event, context):
    
    for record in event['records']:
        
        # Add newline to string
        payload = base64.b64decode(record['data']).decode('utf-8')
        print('payload:', payload)
        
        payload_edited = payload.replace("\\", "")
        row_w_newline = payload_edited[:-1]
        print("Remove last quote and slashes:", row_w_newline)
        
        adjusted_newline = row_w_newline + "\n"
        print("Add newline", adjusted_newline)
        
        # drop quotation marks
        clean_newline = adjusted_newline[1:]
        print("Cleaned payload:", clean_newline)
        
        encoded_newline = base64.b64encode(clean_newline.encode('utf-8'))
        print("AFTER ENCODE", encoded_newline)
        print(type(encoded_newline))
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': encoded_newline
        }
        output.append(output_record)
        
    print(output)

    print('Processed {} records.'.format(len(event['records'])))
    
    return {'records': output}
