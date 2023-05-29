#update route 53
import boto3

# Configure AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_AWS_ACCESS_KEY',
    aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
    region_name='us-west-2'  # Replace with your desired AWS region
)

# Create Route 53 client
route53_client = session.client('route53')

# Update A record IP address
def update_a_record(domain_name, new_ip_address):
    hosted_zone_id = 'your-hosted-zone-id'  # Replace with your hosted zone ID

    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': domain_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': new_ip_address}]
                    }
                }
            ]
        }
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('A record updated successfully.')
    else:
        print('Failed to update A record.')

# Call the function to update the A record
update_a_record('your-domain.com', 'new-ip-address')  # Replace with your domain and new IP address
