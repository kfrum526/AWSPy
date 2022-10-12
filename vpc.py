from distutils.command.config import config
from hashlib import new




import boto3

ec2=boto3.client('ec2')

vpcname = input('What is the name of your VPC: ')


def newvpc(newvpc):
    ec2.create_vpc(
        CidrBlock="10.0.0.0/16",
        AmazonProvidedIpv6CidrBlock=False,
        DryRun=True,
        TagSpecifications=[
            {
            'ResourceType': 'vpc',
            'Tags': [{'Key': 'Name', 'Value': newvpc}]
            }
        ]  
    )

myvpc = ec2.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [vpcname]
                }
            ]
        )
vpcresp = myvpc['Vpcs']


if vpcresp:
    print('VPC already exists')
else:
    newvpc(vpcname)