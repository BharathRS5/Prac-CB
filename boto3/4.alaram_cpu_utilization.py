import boto3

client = boto3.client('cloudwatch')

response = client.put_metric_alarm(
    AlarmName='CPU-Utilization-Alaram',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-0ac49f5b429326b57'
        },
    ],
    Statistic='Maximum',
    Period=60, #1-Minute
    EvaluationPeriods=1, 
    ComparisonOperator='GreaterThanThreshold',
    Unit='Percent',
    Threshold=50.0,
    ActionsEnabled=True, # by default it will be true
    AlarmActions=['arn:aws:sns:us-east-1:704629374558:SNS_Topic_Practice'],
    AlarmDescription='Hi team, this mail is from AWS Cloud Watch your instance cpu is spiked to more than 50 percent, take actions ASAP'
)