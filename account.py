import imp
from re import I
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
)


#     igwd = ec2.describe_internet_gateways(
#     Filters=[
#         {
#             'Name': 'tag:Name',
#             'Values': ['PythonIGW']
#         }
#     ]
# )
# respig = igwd['InternetGateways']

# for i in respig:
#     igwid=i['InternetGatewayId']


# ec2.attach_internet_gateway(
#     InternetGatewayId=igwid,
#     VpcId=idvpc
#     )