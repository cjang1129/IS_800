import boto3

def get_ec2_instances():
    # Create EC2 client for us-east-1 region
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    try:
        # Get all instances
        response = ec2_client.describe_instances()

        # List to store instance details
        instance_details = []

        # Iterate through reservations and instances
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                # Get instance type
                instance_type = instance['InstanceType']

                # Get instance name from tags if it exists
                instance_name = 'N/A'
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            instance_name = tag['Value']
                            break

                # Get instance ID
                instance_id = instance['InstanceId']

                # Get instance state
                instance_state = instance['State']['Name']

                # Add instance details to list
                instance_details.append({
                    'Instance ID': instance_id,
                    'Name': instance_name,
                    'Type': instance_type,
                    'State': instance_state
                })

        # Print instance details
        if instance_details:
            print("\nEC2 Instances in us-east-1:")
            print("-" * 80)
            for instance in instance_details:
                print(f"Instance ID: {instance['Instance ID']}")
                print(f"Name: {instance['Name']}")
                print(f"Type: {instance['Type']}")
                print(f"State: {instance['State']}")
                print("-" * 80)
        else:
            print("No EC2 instances found in us-east-1 region")

    except Exception as e:
        print(f"Error retrieving EC2 instances: {str(e)}")

if __name__ == "__main__":
    get_ec2_instances()
