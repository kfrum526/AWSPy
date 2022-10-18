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

subnet = ec2.describe_subnets(Filters=[{'Name': 'vpc-id','Values': ['vpc-09b4fd70f6d38b41d']}])

subnet1 = subnet['Subnets']

for i in subnet1:
    print(i['SubnetId'])

# [default]
# aws_access_key_id = AKIATZQNSMYR77WEBJZS
# aws_secret_access_key = 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
