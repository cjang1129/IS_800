python3
>>> import boto3
>>> ec2_client = boto3.client('ec2', region_name='us-east-1')
>>> instance_id = 'i-0cfb1e75e74229968'
>>> print(f"Stopping instance: {instance_id}")
... 
Stopping instance: i-0cfb1e75e74229968
>>> ec2_client.stop_instances(InstanceIds=[instance_id])
... 
{'StoppingInstances': [{'InstanceId': 'i-0cfb1e75e74229968', 'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': '4d95ee67-fcd8-4235-a004-4b8ad0917b5a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4d95ee67-fcd8-4235-a004-4b8ad0917b5a', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '411', 'date': 'Thu, 13 Feb 2025 23:18:02 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
>>> waiter = ec2_client.get_waiter('instance_stopped')
... 
>>> waiter.wait(InstanceIds=[instance_id])
... print(f"Instance {instance_id} stopped.")
... 

python3
Instance i-0cfb1e75e74229968 stopped.
>>> 
>>> print(f"Terminating instance: {instance_id}")
... 
Terminating instance: i-0cfb1e75e74229968
>>> ec2_client.terminate_instances(InstanceIds=[instance_id])
... 
{'TerminatingInstances': [{'InstanceId': 'i-0cfb1e75e74229968', 'CurrentState': {'Code': 48, 'Name': 'terminated'}, 'PreviousState': {'Code': 80, 'Name': 'stopped'}}], 'ResponseMetadata': {'RequestId': 'eac9e215-53be-4bb7-9206-bd4019863392', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'eac9e215-53be-4bb7-9206-bd4019863392', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '423', 'date': 'Thu, 13 Feb 2025 23:19:04 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
>>> waiter = ec2_client.get_waiter('instance_terminated')
... 
>>> print(f"Instance {instance_id} terminated.")
Instance i-0cfb1e75e74229968 terminated.
