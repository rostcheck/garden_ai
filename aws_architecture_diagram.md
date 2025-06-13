# Garden AI AWS Architecture Diagram

This document provides instructions for generating an AWS architecture diagram using the Python `diagrams` library.

## Prerequisites

To generate the AWS architecture diagram, you'll need:

1. Python 3.6 or later
2. The `diagrams` library
3. Graphviz (required by the diagrams library)

## Installation

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the diagrams library
pip install diagrams

# Note: Graphviz is required and should be installed system-wide
# For macOS (already installed via brew):
# brew install graphviz

# For Ubuntu/Debian:
# sudo apt-get install graphviz

# For Windows:
# Download and install from https://graphviz.org/download/
```

## Generating the Diagram

1. Run the provided Python script (make sure your virtual environment is activated):

```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the script
python3 aws_architecture_diagram.py
```

2. This will generate a file named `aws_architecture_diagram.png` in the current directory.

## About the Diagram

The generated diagram shows a simplified view of the Garden AI architecture using official AWS service icons. It includes:

- Edge Device (IoT Camera on Raspberry Pi)
- AWS Cloud components:
  - S3 for image storage and static website hosting
  - DynamoDB for storing plant status, AI summaries, and messages
  - EventBridge for scheduled triggers
  - Lambda for processing images and CRUD operations
  - Amazon Bedrock Nova Pro for AI analysis
  - Cognito User Pool for authentication
  - API Gateway for web interface communication
- Gardener interaction through the web interface

The diagram focuses on components and data flow direction, providing a clear visual representation of how the system works.