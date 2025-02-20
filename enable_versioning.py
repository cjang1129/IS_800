import boto3

s3 = boto3.client('s3')
bucket_name = 'python-cj-is800-bucket'
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={'Status': 'Enabled'}
)
print(f'Versioning enabled for bucket {bucket_name}!')

