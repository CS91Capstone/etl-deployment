import json
import subprocess
import os
import boto3
from zipfile import ZipFile

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def package_lambda(path: str, repo_name: str, deploy_file: str, lambda_folder: str):
    os.chdir("/tmp") # /tmp (path)
    output = subprocess.getoutput([f"git clone {path}"])
    print(output)
    os.chdir(f"/tmp/{repo_name}/endpoints/{lambda_folder}") # /tmp/{repo_name}/endpoints/{lambda_folder}   (path)
    print(os.getcwd())
    print(subprocess.getoutput([f"pip install --target ../package -r requirements.txt"]))
    os.chdir(f"/tmp/{repo_name}/endpoints/package") # /tmp/{repo_name}/endpoints/package   (path)
    # path to folder which needs to be zipped
    directory = f"./"

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # writing files to a zipfile
    with ZipFile(f"/tmp/{deploy_file}",'w') as zip:
        # writing each file one by one
        for file in file_paths:
            print(file)
            zip.write(file)
        os.chdir(f"/tmp/{repo_name}/endpoints/{lambda_folder}") # /tmp/{repo_name}/endpoints/{lambda_folder} (path)
        zip.write(f"{lambda_folder}.py")
    os.chdir("/tmp") # /tmp (path)

def deploy_s3(bucket: str, key: str, body: str):
    # print(subprocess.getoutput([f"pwd"]))
    # print(get_all_file_paths("./"))
    print(os.getcwd())
    zip = ZipFile(body)
    # print(zip.namelist())
    s3_resource = boto3.resource('s3')

    # Write buffer to S3 object
    s3_resource.meta.client.upload_file(body, bucket, key)
        
def get_configurations(configurations):
    # configurations: dict = json.loads(event['body'])
    repo_path: str = configurations['repo_path']
    username: str = configurations['username']
    token: str = configurations['token']
    index: int = repo_path.find('github.com')
    credential_path: str = repo_path[:index] + username + ":" + token + "@" + repo_path[index:]
    configurations['credential_path'] = credential_path
    return configurations

def lambda_handler(event, context):
    configurations: dict = get_configurations(event)
    print(configurations)
    username: str = configurations['username']
    token: str = configurations['token']
    repo_name: str = configurations['repo_name']
    lambda_folder: str = configurations['lambda_folder']
    repo_path: str = configurations['repo_path']
    credential_path : str = configurations['credential_path']
    bucket_name: str = configurations['bucket_name']
    bucket_key: str = configurations['bucket_key']
    bucket_body: str = configurations['bucket_body']

    package_lambda(path=credential_path, repo_name=repo_name, deploy_file=bucket_body, lambda_folder=lambda_folder)
    deploy_s3(bucket=bucket_name, key=bucket_key, body=bucket_body)

    return {
        'statusCode': 200,
        'body': json.dumps('Congratz on your deploy!')
    }