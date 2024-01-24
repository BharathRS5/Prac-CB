import boto3

client = boto3.client('sns')

response = client.create_topic(
    Name='SNS_Topic_Practice',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Boto_SNS'
        },
    ]
)

print(response)
topic_arn = response['TopicArn']
print(f"SNS topic created with ARN: {topic_arn}")