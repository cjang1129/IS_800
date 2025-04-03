cj@Chans-MacBook-Air ~ % python3
Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> ec2 = boto3.resource('ec2', region_name='us-east-1')
>>> instance = ec2.create_instances(
...     ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (Free Tier Eligi\
ble)
...     MinCount=1,
...     MaxCount=1,
...     InstanceType='t2.micro',
...     KeyName='firstkey',  # Ensure you have created this key pair
...     TagSpecifications=[
...         {
...             'ResourceType': 'instance',
...             'Tags': [
...                 {'Key': 'Name', 'Value': 'MyPythonEC2Instance'}
...             ]
...         }
...     ]
... )
... 
>>> print(f'Created instance with ID: {instance[0].id}')
... 
Created instance with ID: i-0cfb1e75e74229968
