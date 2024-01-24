import boto3

client = boto3.client('ec2')

ami_id = 'ami-0005e0cfe09cc9050'
instance_type = 't2.micro'
public_key = 'Practice_Key_Public'

response = client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=public_key,
    MinCount=1,
    MaxCount=1,
    Monitoring={
        'Enabled': True
    },
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Boto_Instance'
                },
            ]
        }
    ]
)

print(response)
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance created with ID: {instance_id}")
