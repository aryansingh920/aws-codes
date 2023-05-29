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


@app.get("/start-ec2")
def start_ec2():
    instance_id = 'your-instance-id'  # Replace with your instance ID
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    return {"message": "EC2 instance starting"}


@app.get("/stop-ec2")
def stop_ec2():
    instance_id = 'your-instance-id'  # Replace with your instance ID
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    return {"message": "EC2 instance stopping"}


@app.get("/get-private-ip")
def get_private_ip():
    instance_id = 'your-instance-id'  # Replace with your instance ID
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    private_ip = response['Reservations'][0]['Instances'][0]['PrivateIpAddress']
    return {"private_ip": private_ip}

# from fastapi import FastAPI
# import boto3

# app = FastAPI()

# # Configure AWS credentials
# session = boto3.Session(
#     aws_access_key_id='YOUR_AWS_ACCESS_KEY',
#     aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
#     region_name='us-west-2'  # Replace with your desired AWS region
# )

# # Create EC2 client
# ec2_client = session.client('ec2')


# @app.get("/get-public-ip")
# def get_public_ip():
#     instance_id = 'your-instance-id'  # Replace with your instance ID
#     response = ec2_client.describe_instances(InstanceIds=[instance_id])
#     public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
#     return {"public_ip": public_ip}
