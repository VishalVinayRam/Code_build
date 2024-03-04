import boto3
import schedule
import time

# Replace these values with your own AWS credentials and project information
aws_access_key_id = 'ASIARLRYIN2AOS6LPB4M'
aws_secret_access_key = 'Z6GoCKylmg4SwSYD2ACWUcwAPSgun7SntRYHIiV2'
region_name = 'ap-south-1'
codebuild_project_name = 'FreeStyle6'

# Initialize AWS CodeBuild client
codebuild_client = boto3.client('codebuild', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key, region_name=region_name)

def run_codebuild():
    try:
        print(f"Running CodeBuild project: {codebuild_project_name}")
        response = codebuild_client.start_build(projectName=codebuild_project_name)
        build_id = response['build']['id']
        print(f"Build started with ID: {build_id}")
    except Exception as e:
        print(f"Error starting CodeBuild: {str(e)}")

# Schedule job to run every 5 minutes
schedule.every(5).minutes.do(run_codebuild)

# Run the job indefinitely
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Script terminated by user.")
        break
    except Exception as e:
        print(f"Error in the main lo")
