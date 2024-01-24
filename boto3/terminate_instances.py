import boto3

client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=[
        'i-091406b2f203aaa8b',
    ]
)

print(response)
# print(f"EC2 instance created with ID: {instance_id}")