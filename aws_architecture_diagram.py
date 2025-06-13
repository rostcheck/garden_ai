#!/usr/bin/env python3
"""
Garden AI AWS Architecture Diagram Generator
Uses diagrams library to create an AWS architecture diagram
"""

from diagrams import Diagram, Cluster, Edge, Node
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.integration import Eventbridge
from diagrams.aws.network import APIGateway
from diagrams.aws.ml import Bedrock
from diagrams.aws.security import Cognito
from diagrams.aws.iot import IotCamera
from diagrams.generic.device import Mobile  # For Web App/Gardener

# Set diagram attributes
graph_attr = {
}

# Edge attributes to ensure connections
edge_attr = {
}

# Node attributes
node_attr = {
    "fontsize": "12",     
}

# Create the diagram
with Diagram("Garden AI Architecture", show=False, filename="aws_architecture_diagram", 
             outformat="png", graph_attr=graph_attr, edge_attr=edge_attr, node_attr=node_attr):
    
    # Edge Device
    with Cluster("Edge Device"):
        raspberry_pi = IotCamera("IoT Camera\nRaspberry Pi")
    
    # AWS Cloud
    with Cluster("AWS Cloud"):
        # Storage
        s3_images = S3("S3\nImage Repository")
        
        # Database
        dynamodb = Dynamodb("DynamoDB\nPlant Status\nAI Summaries\nMessages")
        
        # Processing
        eventbridge = Eventbridge("EventBridge\nScheduled Trigger")
        lambda_function = Lambda("Lambda\nProcessing Function")
        bedrock = Bedrock("Amazon Bedrock\nNova Pro")
        
        # Web Interface
        api_gateway = APIGateway("API Gateway")
        web_app = S3("S3\nStatic Website")
        crud_lambda = Lambda("Lambda\nCRUD Operations")
        
        # Authentication
        cognito = Cognito("Cognito\nUser Pool")
    
    # Human Interaction
    gardener = Mobile("Gardener\nWeb Interface")
    
    # Connections with proper directionality
    # Edge device to S3
    raspberry_pi >> Edge(label="Upload Images") >> s3_images
    
    # EventBridge to Lambda - direct connection
    eventbridge >> Edge(label="Trigger") >> lambda_function
    
    # Lambda reads from S3
    s3_images >> Edge(label="Read Images") >> lambda_function
    
    # Lambda reads/writes to DynamoDB (bidirectional)
    lambda_function << Edge(label="Read/Write") >> dynamodb
    
    # Lambda to Bedrock (correct direction)
    lambda_function >> Edge(label="Send Image") >> bedrock
    lambda_function << Edge(label="Return Analysis") << bedrock
    
    # Web interface connections (corrected)
    web_app >> Edge(label="Serve") >> gardener
    gardener >> Edge(label="API Calls") >> api_gateway
    
    # API Gateway to Cognito and CRUD Lambda
    api_gateway << Edge(label="Authenticate") >> cognito
    api_gateway >> Edge(label="Process") >> crud_lambda
    
    # CRUD Lambda to DynamoDB (bidirectional)
    crud_lambda << Edge(label="Read/Write") >> dynamodb

print("Diagram generated as 'aws_architecture_diagram.png'")