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

### Potential Feature
- Create additional Lambda function and endpoint to allow developer to push ALL code in the `/endpoints` folder into S3 bucket
  - One problem with this endpoint is the timeout limit on AWS API Gateway which is 30 seconds. It would take more than 30 seconds to push ALL code into S3 bucket.
  - Potential workaround:
    - Make Lambda function and API Gateway async (User wouldn't be able to receive response back from the Lambda function)
