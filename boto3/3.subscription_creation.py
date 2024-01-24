import boto3

client = boto3.client('sns')

response = client.subscribe(
    TopicArn='arn:aws:sns:us-east-1:704629374558:SNS_Topic_Practice',
    Protocol='email',
    Endpoint='rsbharathrsb@gmail.com'
)

print(response)
subscription_arn = response['SubscriptionArn']
print(f"SNS subscription created with ARN: {subscription_arn}")