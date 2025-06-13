# Garden AI - System Architecture

## System Overview

Garden AI is an experimental plant monitoring system that leverages AWS cloud services and AI to analyze plant health and facilitate communication between the system and human gardeners. The architecture is designed to study AI/human interaction patterns over the timescale of a long-running problem, such as growing a plant, with a focus on asynchronous communication and independent actors.

## Architecture Diagram

For a visual representation of this architecture, please see [architecture_diagram.md](architecture_diagram.md).

## Architecture Components

### 1. Edge Device Setup

The edge component consists of:

- **Raspberry Pi**: Acts as the local computing device
- **Camera Module**: Attached to the Raspberry Pi for image capture
- **Local Storage**: Temporary storage for images before upload
- **Python Script**: Handles image capture and upload to AWS
- **Cron Jobs**: Schedule regular image captures (1-2 times daily)

The edge device is responsible for capturing high-quality images of the plant at scheduled intervals and securely uploading them to AWS for processing.

### 2. AWS Cloud Components

#### Storage Layer

- **Amazon S3 Bucket**: 
  - Primary storage for all plant images
  - Organized chronologically for tracking plant growth over time

- **Amazon DynamoDB**:
  - Stores plant status information and metrics
  - Maintains AI-generated summaries and observations over time
  - Serves as the message repository for AI-gardener communication
  - Tracks historical data and trends

#### Processing & AI Analysis

- **Amazon EventBridge**:
  - Schedules regular invocations of the Lambda function
  - Decouples image capture from analysis for resilience

- **AWS Lambda**:
  - Triggered by EventBridge on a scheduled basis
  - Checks for new images in S3
  - Retrieves historical data and previous summaries from DynamoDB
  - Prepares and sends images to Amazon Bedrock
  - Processes AI analysis results
  - Updates DynamoDB with new plant status information and summaries
  - Writes messages for the gardener when needed

- **Amazon Bedrock Nova Pro**:
  - Foundation model that analyzes plant images
  - Identifies plant health issues, growth patterns, and care needs
  - Provides comprehensive assessment in natural language
  - Suggests specific actions for the gardener when needed

#### Communication System

- **Web Application**:
  - Hosted as a static website on S3
  - Provides interface for gardeners to view plant status and history
  - Displays messages from the AI system
  - Allows gardeners to respond with messages and actions taken

- **Amazon API Gateway**:
  - Provides secure endpoints for the web application
  - Routes requests to appropriate Lambda functions

- **Authentication Lambda**:
  - Handles user authentication and authorization
  - Ensures secure access to the system

## Data Flow

1. **Image Capture**:
   - Raspberry Pi captures plant images at scheduled intervals
   - Images are stored locally and then uploaded to the designated S3 bucket

2. **Scheduled Analysis**:
   - EventBridge triggers Lambda function at configured times
   - Lambda checks for new images in S3
   - Lambda retrieves historical data and previous AI summaries from DynamoDB

3. **AI Processing**:
   - Lambda sends the latest image and context to Amazon Bedrock Nova Pro
   - Nova Pro analyzes the image and returns detailed assessment
   - Lambda processes the AI analysis and generates updated summaries
   - Results and summaries are stored in DynamoDB

4. **Communication**:
   - AI writes messages to DynamoDB when observations or recommendations are available
   - Gardener accesses the web application to view plant status and AI messages
   - Gardener responds by writing messages about actions taken
   - All communication is asynchronous, respecting the natural timescale of plant growth

## Key Advantages

- **Asynchronous Communication**: Aligns with the natural pace of plant growth
- **Independent Actors**: AI and gardener operate independently without requiring immediate responses
- **Historical Context**: AI maintains and evolves understanding through summaries
- **Experimental Data**: System captures interaction patterns for research purposes
- **Resilient Design**: Decoupled components reduce dependencies and points of failure

## Security Considerations

- Edge device uses secure AWS credentials for S3 uploads
- Web application implements proper authentication
- API Gateway enforces HTTPS and authentication
- DynamoDB access is controlled through fine-grained IAM policies

## Scalability

While designed for a single plant monitoring setup, the architecture can be scaled to monitor multiple plants by:

1. Adding more edge devices
2. Implementing plant identification in the Lambda function
3. Expanding the DynamoDB schema to track multiple plants
4. Enhancing the web interface to display multiple plants