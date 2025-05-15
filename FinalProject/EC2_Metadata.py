import boto3

client = boto3.client('ec2')
response = client.describe_instances()
for instance in response['Reservations']:
    for instance in instance['Instances']:
        print(instance['InstanceId'])
