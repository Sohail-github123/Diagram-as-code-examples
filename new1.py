from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.engagement import SimpleEmailServiceSes,SES
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito

# Create Diagram
with Diagram("AWS Architecture", show=True):
    
    # Define AWS Services
    api_gateway = APIGateway("API Gateway")
    lambda_function = Lambda("Lambda Function")
    rds = RDS("RDS Database")
    s3 = S3("S3 Bucket")
    ses = SES("SES Email Service")
    cognito = Cognito("Cognito User Pool")

    # Define Service Interactions
    api_gateway >> lambda_function
    lambda_function >> rds
    lambda_function >> s3
    lambda_function >> ses
    lambda_function >> cognito
