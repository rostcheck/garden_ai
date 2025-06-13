# Garden AI

An experimental plant monitoring system that uses AI to analyze plant health and communicate with gardeners.

## Overview

Garden AI is a smart plant monitoring system that combines edge computing with AWS cloud services and AI to provide automated plant care assistance. The system captures regular images of plants, analyzes their health using AI, and communicates with human gardeners when intervention is needed.

This project is designed to study interaction patterns between AI and human actors over the longer timescale of plant growth. By creating an asynchronous communication framework where both the AI and gardener operate independently, the system allows for observation of how these interactions evolve over time.

## Features

- Automated image capture of plants at regular intervals
- AI-powered analysis of plant health and growth
- Identification of potential issues (diseases, pests, nutrient deficiencies)
- Automated notifications to gardeners when action is needed
- Two-way communication between the system and gardeners
- Historical tracking of plant growth and health

## System Components

- **Edge Device**: Raspberry Pi with camera module
- **Cloud Infrastructure**: AWS S3, Lambda, DynamoDB, SNS
- **AI Analysis**: Amazon Bedrock Nova Pro foundation model
- **Communication**: SNS notifications and API Gateway

## Getting Started

1. Set up the Raspberry Pi with the camera module
2. Deploy the AWS infrastructure using the provided templates
3. Configure the edge device to capture and upload images
4. Set up notification preferences for the gardener

## Architecture

For detailed information about the system architecture, please see [architecture.md](architecture.md).

## Project Status

This project is currently in experimental phase.

## License

[Specify your license here]