# Reddit Data Engineering Pipeline
This project extracts data from the "dataengineering" subreddit, selects relevant fields, saves it into a CSV file, and uploads the file to an AWS S3 bucket. The workflow is deployed on an EC2 instance running Ubuntu and is orchestrated using Apache Airflow.

## Project Overview
Data Extraction: Connect to the Reddit API and extract data from the "dataengineering" subreddit.
Data Selection & Loading: Choose useful data fields, save the data into a CSV file.
Upload to S3: Load the CSV file into an AWS S3 bucket.
Deployment: Run the pipeline on an EC2 instance (Ubuntu) with Apache Airflow to schedule and manage tasks.
## Prerequisites
AWS Account: Set up an S3 bucket and an EC2 instance running Ubuntu.
Apache Airflow: Installed and configured on your EC2 instance.
Python Libraries: requests, pandas, boto3, and python-dotenv (for environment variable management).
Reddit API: Obtain API credentials (App ID, Secret, Username, and Password).
