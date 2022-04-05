# ETL Deployment

#### WARNING - MUST BE RUN FROM INSIDE THE DIRECTORY THAT THE DOCKER FILE IS IN

&nbsp;

Steps:
- Logs docker in to AWS using local AWS cli credentials
- Builds docker image using Dockerfile
- Tags docker image
- Upload docker image to ECR

&nbsp;

TO Run:

python3 deploy.py {tag} 

&nbsp;

Note on lambda_function.py:
- A lambda function to process and deploy other lambda functions from GitHub to s3 bucket
- Must include https://github.com/lambci/git-lambda-layer in the layer of the lambda function
