# CloudFormationTemplates

This directory contains YAML scripts for use with AWS CloudFormation.
All of the templates assume the following things:
* There are no resources already using the custom names defined in the templates
* The template is being used on an account with the AWS account ID of 949449017276 
* There is an S3Bucket by the name d3-capstone-bucket
* The file paths for the Lambda function code are correct and that there are zip files at the locations given in the Lambda Function specifications
* The lambda handler name defined for each of the Lambda Functions created matches the specifications found in the each lambda's code
* There is an rds database with the specifications and log in credentials defined within the templates (applicable for the CampsiteEndpoints templates)


## CodeDeployment.yaml

This template defines resources used for deploying code from github to the specified S3Bucket.
The CodeDeployment.yaml template creates the following AWS resources:
* 1x AWS::ApiGateway::RestApi
* 2x AWS::ApiGateway::Resource
* 1x AWS::ApiGatewat::Model
* 1x AWS::ApiGateway::Method
* 1x AWS::ApiGateway::Stage	
* 1x AWS::ApiGateway::Deployment
* 1x AWS::Lambda::Function
* 2x AWS::IAM::Role
* 1x AWS::IAM::Policy


## CampsiteEndpoints.yaml

This template defines the resources for an AWS Rest API serving Campsite data.
The CampsiteEndpoints.yaml template creates the following AWS resources:
* 1x AWS::ApiGateway::RestApi
* 10x AWS::ApiGateway::Resource
* 1x AWS::ApiGatewat::Model
* 8x AWS::ApiGateway::Method
* 1x AWS::ApiGateway::Stage
* 1x AWS::ApiGateway::Deployment
* 8x AWS::Lambda::Function
* 16x AWS::IAM::Role
* 8x AWS::IAM::Policy


## CampsiteEndpoints_Params.yaml

This template defines the resources for an AWS Rest API serving Campsite data. This template differs from the CampsiteEnpoints.yaml template only in that it uses a CloudFormation parameter to define MYSQL_PASS when the CloudFormation stack is created instead of having the password hardcoded in the template.
The CampsiteEndpoints_Params.yaml template creates the following AWS resources:
* 1x AWS::ApiGateway::RestApi
* 10x AWS::ApiGateway::Resource
* 1x AWS::ApiGatewat::Model
* 8x AWS::ApiGateway::Method
* 1x AWS::ApiGateway::Stage
* 1x AWS::ApiGateway::Deployment
* 8x AWS::Lambda::Function
* 16x AWS::IAM::Role
* 8x AWS::IAM::Policy