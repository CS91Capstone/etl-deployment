# ETL Deployment
## Developer API
The developer API is located inside the `/endpoints/deploy-development`. It is used to pull Lambda function code from github, package them, and store them in S3 Bucket named d3-capstone-bucket.
- This Lambda function can be hooked up with AWS API Gateway to form an API endpoint for developer or it can be invoke in a Github Actions.
- It should be zipped (deploy-development.zip) and put into an S3 Bucket named d3-capstone-bucket and with `/deploy/development` pathing. So that it can be referred in the Cloudformation stack.
- When created inside AWS, the Lambda function must be given put object access to S3 bucket. It should also be provided a layer named [git-lambda-layer](https://github.com/lambci/git-lambda-layer)

### Usage
The Lambda function can be integrated with AWS API Gateway which can then be called via Postman.
- This Lambda function assume the other Lambda function which to be pulled from Github to S3 be stored in specific directory.
  - All Lambda functions should be store in `/endpoints/{lambda_name}/{lambda_name}.py`
- The API Gateway should be set up as a POST request with the following body provided when called
  ```json
  {
    "username":"github username",
    "token":"github token",
    "repo_name":"etl-api",
    "lambda_folder":"campsite_accessible",
    "repo_path":"https://github.com/BigDataCapstone/etl-api",
    "bucket_name":"d3-capstone-bucket",
    "bucket_key":"api/development/campsite_accessible.zip",
    "bucket_body":"campsite_accessible.zip"
  }
  ```
- When used in Github Actions. The [invoke-aws-lambda](https://github.com/marketplace/actions/invoke-aws-lambda) action can be used. A body with same format as above would then need to be present in the Payload section of that action.

## CloudFormation Templates

This directory contains YAML templates for use with AWS CloudFormation.
All of the templates assume the following things:
* There are no resources already using the custom names defined in the templates
* The template is being used on an account with the AWS account ID of 949449017276 
* There is an S3Bucket by the name d3-capstone-bucket
* The file paths for the Lambda function code are correct and that there are zip files at the locations given in the Lambda Function specifications
* The lambda handler name defined for each of the Lambda Functions created matches the specifications found in the each lambda's code
* There is an RDS database with the specifications and log in credentials defined within the templates (applicable for the CampsiteEndpoints templates)

If you plan on using these templates whithout all of these assumptions being true then you will need to edit the templates. These are some, but potentially not all, of the changes that will need to be made to the templates:
* Change the AWS account information defined in the template (e.g. AWS account ID)
* Change all S3 Bucket URI within the template to match the S3 you intend to use
* Change the lambda handler name defined in the templates for each Lambda Function (if they don't already match)
* The RDS database will need to be set up and the database access variables for each Lambda Function in the template will need to be updated

### CodeDeployment.yaml

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


### CampsiteEndpoints.yaml

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


### CampsiteEndpoints_Params.yaml

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
