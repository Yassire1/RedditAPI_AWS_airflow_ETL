from datetime import datetime,timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import requests.auth
import json
import s3fs
import os
from dotenv import load_dotenv


def Extract_data(file_path='extracted_data.json'):
    load_dotenv()
    APP_ID = os.getenv("APP_ID")
    secret_id = os.getenv("SECRET_ID")
    base_url = 'https://www.reddit.com/'

    # Generate the access token
    data = {
        'grant_type': 'password',
        'username': os.getenv("REDDIT_USERNAME"),
        'password': os.getenv("REDDIT_PASSWORD")
    }
    auth = requests.auth.HTTPBasicAuth(APP_ID, secret_id)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    r = requests.post(
        base_url + 'api/v1/access_token',
        data=data,
        headers=headers,
        auth=auth
    )

    ACCES_TOKEN = r.json()['access_token']
    headers['Authorization'] = f'bearer {ACCES_TOKEN}'
    
    # Request data from the Reddit API
    try: 
        res = requests.get('https://oauth.reddit.com/r/dataengineering/hot', headers=headers, params={'limit': '200'})
        res.raise_for_status()
        posts = res.json()['data']['children']
    except Exception as e:
        print(f"Error in requesting phase: {e}")
        return

    # Save data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(posts, f)
    print(f"Data extracted and saved to {file_path}")

def Load_Data(file_path='extracted_data.json'):
    # Read data from the JSON file
    with open(file_path, 'r') as f:
        posts = json.load(f)
    
    # Process and load data into a DataFrame
    df = pd.DataFrame([{
        'title': row['data'].get('title'),
        'subreddit': row['data'].get('subreddit'),
        'selftext': row['data'].get('selftext'),
        'upvote_ratio': row['data'].get('upvote_ratio'),
        'ups': row['data'].get('ups'),
        'downs': row['data'].get('downs'),
        'score': row['data'].get('score'),
        'user_name': row['data'].get('author_fullname')
    } for row in posts])

    # Save the data to a CSV file
    df.to_csv("s3://your_s3_bucket_name/Reddit_api_data.csv", index=False)
    print("Data loaded and saved to Reddit_api_data.csv")


default_args= {
    'owner' : 'airflow',
    'start_day': days_ago(0),
    'email': ['yassire.ammouri@etu.uae.ac.ma'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta (minutes = 5),
}

dag= DAG(
    'Reddit_airflow',
    default_args=default_args,
    start_date = datetime(2024,11,3)
    schedule_interval=timedelta(days=1),
    
    description='Reddit API  data extruction with airflow',
)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=Extract_data,
    op_kwargs={'file_path': 'extracted_data.json'}, 
    dag= dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=Load_Data,
    op_kwargs={'file_path': 'extracted_data.json'},  
    dag= dag
)

extract_task >> load_task