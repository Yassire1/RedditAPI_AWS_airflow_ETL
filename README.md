# Reddit Data Engineering Pipeline

This project extracts data from the "dataengineering" subreddit, filters and loads it into a CSV file, and uploads the file to an AWS S3 bucket. The pipeline is deployed on an EC2 instance running Ubuntu and orchestrated using Apache Airflow.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Airflow DAG Configuration](#airflow-dag-configuration)
- [License](#license)

## Project Overview

1. **Data Extraction**: Connect to the Reddit API and extract data from the "dataengineering" subreddit.
2. **Data Selection & Loading**: Select useful data fields, store the data in a CSV file.
3. **Upload to S3**: Upload the CSV file to an AWS S3 bucket.
4. **Deployment**: Run the pipeline on an EC2 instance (Ubuntu) with Apache Airflow for orchestration.

## Prerequisites

To set up this project, ensure you have the following:

- **AWS Account**: Access to an S3 bucket and an EC2 instance running Ubuntu.
- **Apache Airflow**: Installed and configured on your EC2 instance.
- **Python Libraries**: Install `requests`, `pandas`, `boto3`, and `python-dotenv` (for environment variable management).
- **Reddit API Credentials**: Obtain credentials for your Reddit app, including App ID, Secret, Username, and Password.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Yassire1/RedditAPI_AWS_airflow_ETL.git
   cd RedditAPI_AWS_airflow_ETL
