import subprocess
import argparse


# WARNING - MUST BE RUN FROM INSIDE THE DIRECTORY THAT THE DOCKER FILE IS IN

parser = argparse.ArgumentParser(description='Deploy')
parser.add_argument('tag', type=str, help='Tag used for Docker Image')


def deploy_docker(tag: str):
    subprocess.getoutput(["aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 949449017276.dkr.ecr.us-west-2.amazonaws.com"])
    subprocess.getoutput(["docker build -t lambda_etl_api ."])
    subprocess.getoutput([f"docker tag lambda_etl_api:latest 949449017276.dkr.ecr.us-west-2.amazonaws.com/lambda_etl_api:{tag}"])
    subprocess.getoutput([f"docker push 949449017276.dkr.ecr.us-west-2.amazonaws.com/lambda_etl_api:{tag}"])


if __name__ == "__main__":
    args = parser.parse_args()
    tag: str = args.tag

    deploy_docker(tag=tag)