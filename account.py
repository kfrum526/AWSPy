import imp
from re import I
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
)