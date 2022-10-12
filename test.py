from pydoc import cli
import boto3

ec2=boto3.client('ec2')

myvpc = ec2.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['AWSCLI']
        }
    ]
)

resp = myvpc['Vpcs']

print(resp)