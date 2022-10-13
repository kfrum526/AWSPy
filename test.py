###############################################################################################
###############################################################################################
###############################################################################################
## This Script is for testing small part of code to add to main code once confirmed it works ##
###############################################################################################
###############################################################################################
###############################################################################################


from pydoc import cli
import boto3

ec2=boto3.client('ec2')


myvpc = ec2.describe_vpcs(Filters=[{'Name': 'tag:Name','Values': ['AWSCLI']}])

resp = myvpc['Vpcs']

for vpc in resp:
    vpcid=vpc['VpcId']
#vpcid = resp['VpcId']

print(vpcid)


# [default]
# aws_access_key_id = AKIATZQNSMYR77WEBJZS
# aws_secret_access_key = 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
