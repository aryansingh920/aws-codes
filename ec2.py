from fastapi import FastAPI
import boto3

app = FastAPI()

# Configure AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_AWS_ACCESS_KEY',
    aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
    region_name='us-west-2'  # Replace with your desired AWS region
)

# Create EC2 client
ec2_client = session.client('ec2')


@app.get("/get-public-ip")
def get_public_ip():
    instance_id = 'your-instance-id'  # Replace with your instance ID
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return {"public_ip": public_ip}
