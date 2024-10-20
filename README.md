# Bedrock Lambda Function with API Gateway

This project sets up a serverless application using AWS Lambda and API Gateway to query the AWS Bedrock service.

## File Descriptions

### lambda_handler.py
This is the main Lambda function code. It:
- Loads configuration from `bedrock_config.json`
- Assumes an IAM role for Bedrock access
- Queries the Bedrock service with user input
- Formats and returns the response


### bedrock_config.json
Configuration file containing:
- AWS credentials
- Bedrock model settings
- IAM role ARN for Bedrock access

### template.yaml
AWS SAM template that defines the serverless application. It:
- Creates a Lambda function
- Sets up an API Gateway endpoint
- Defines an IAM role for Bedrock access

### Dockerfile
Sets up a local development environment. It:
- Uses Python 3.9
- Installs AWS CLI and required Python packages
- Sets up the environment to run SAM local API

### create_deployment_package.py
Script to create a deployment package for Lambda. It:
- Installs dependencies
- Creates a zip file with the Lambda function and its dependencies
- Provides formatted output of the process

## Usage

1. Update `bedrock_config.json` with your AWS credentials and Bedrock settings.
2. Use the Dockerfile for local development and testing.
3. Run `create_deployment_package.py` to create a deployment package.
4. Use AWS SAM to deploy the application to AWS.

## Security Note

Ensure that `bedrock_config.json` is not committed to version control as it contains sensitive information.
