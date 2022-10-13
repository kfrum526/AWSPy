from distutils.command.config import config
from hashlib import new
from re import sub



## import module
import boto3

## Calls boto3 ec2 client
ec2=boto3.client('ec2')

#######################################
########## VPC CREATION ###############
#######################################

## Get VPC name
vpcname = input('What is the name of your VPC: ')
## prompt for cidrblock
cidrblock = input('What is your VPC CIDR block: ')

## Function to create new VPC's
def newvpc(newvpc):
    ec2.create_vpc(
        CidrBlock=cidrblock,
        AmazonProvidedIpv6CidrBlock=False,
        #DryRun=True,
        TagSpecifications=[
            {
            'ResourceType': 'vpc',
            'Tags': [{'Key': 'Name', 'Value': newvpc}]
            }
        ]  
    )

## describe VPC's ## Tried to put this in a function then call it in a variable but couldn't get a response for the check
myvpc = ec2.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [vpcname]
                },
                {
                    'Name': 'cidr-block-association.cidr-block',
                    'Values': [cidrblock]
                }
            ]
        )

## VPC name response check
vpcresp = myvpc['Vpcs']

# if VPC name comes back then echo it exists and ends script else builds the VPC with the name
if vpcresp:
    print('VPC already exists')
    exit()
else:
     newvpc(vpcname)

#######################################
########## Subnet CREATION ############
#######################################


## Function that gets VPC ID from what you created
## Asks how many subnets you want with CIDR range
## Then adds this to the VPC
def create_subnet():
    # Describes VPC with name filter, specified in creation sets to variable
    vpcdesc = ec2.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [vpcname]
            }
        ]
    )

    # Gets a response from variable with a dictionary
    resp = vpcdesc['Vpcs']

    # Since you are narrowing it down it'll only find the VPC ID of the one you created
    for vpc in resp:
        vpcid=vpc['VpcId']

    # Prompt for name of subnets
    subnetname = input('What is the name of your subnet: ')
    # Prompt for CIDR Range
    subnetcidr = input('What is your subnet CIDR range: ')

    # Subnet Creation to the VPC created previosly
    ec2.create_subnet(
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': subnetname
                    },
                ]
            },
        ],
        CidrBlock=subnetcidr,
        VpcId=vpcid
    )

## Prompt for how many subnets you are building
subnetcount = int(input('How many subnets do you want to create: '))

## Starting from 0 adding one each time til the number you put in the prormpt it will run the create subnet function
for num in range(0, subnetcount, +1):
    create_subnet()