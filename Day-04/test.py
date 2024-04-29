import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='kojo-s3-bucket-demo',
)

response = client.get_bucket_acl(
    Bucket= 'kojo-s3-bucket-demo',
)




