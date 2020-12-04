import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket_name = 'bucket-name'
    bucket = s3.Bucket(bucket_name)

    for object in bucket.objects.all():
        if '/' not in object.key:
            print('deleting ' + object.key)
            s3.Object(bucket_name, object.key).delete()
    
    return {
        'statusCode': 200,
        'body': 'Root folder files deleted, folders preserved'
    }

