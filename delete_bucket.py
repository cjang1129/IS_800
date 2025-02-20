import boto3

s3 = boto3.client('s3')
bucket_name = 'python-cj-is800-bucket'
s3.delete_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} deleted successfully!')

