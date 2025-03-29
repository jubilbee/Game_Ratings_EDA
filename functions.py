import pandas as pd

import requests
from requests import post
import os
import time

def load_or_fetch_data(csv_file_path: str, api_url: str, data: str) -> pd.DataFrame:
    """
    Load data from a CSV file if it exists. If the file does not exist, 
    fetch data from an API, save it to the CSV file, and return it as a DataFrame.

    Args:
        csv_file_path (str): The path to the CSV file.
        api_url (str): The base URL of the API to fetch data from.

    Returns:
        pd.DataFrame: The data loaded from the CSV or fetched from the API.
    """
    # Check if the csv file exists
    if os.path.exists(csv_file_path):
        print(f"CSV file '{csv_file_path}' found. Loading data from CSV.")
        return pd.read_csv(csv_file_path)
    else:
        print(f"CSV file '{csv_file_path}' not found. Fetching data from API.")
        
        # Set Client ID and access token
        client_id = '785ilpg2b1u4z4jyvw10cysnnyojpi'
        access_token = 'ntxl8cihla4pl5fdinfiorq1yd9eki'

        results = []
        limit = 500 # Max limit for IGDB's API
        offset = 0

        while True:
            # Make the API request with limit and offset
            response = requests.post(
                f'{api_url}',
                headers={
                    'Client-ID': client_id,
                    'Authorization': f'Bearer {access_token}'
                },
                data=f'{data} limit {limit}; offset {offset};'
            )
            
            # Check the response status code
            if response.status_code != 200:
                print(f"Request failed with status code {response.status_code}")
                break

            try:
                response_json = response.json()
            except ValueError as e:
                print(f"JSON decode error: {e}")
                break

            # Check if no more results
            if not response_json:
                break
            
            # Append the results to the list
            results.extend(response_json)
            
            # Increment the offset
            offset += limit

            # Add a delay to comply with rate limits (250 milliseconds)
            time.sleep(0.25)
           
        # Create csv file
        directory = os.path.dirname(csv_file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        df = pd.DataFrame(results)
        df.to_csv(csv_file_path, index=False)
        print(f"Data fetched and saved to '{csv_file_path}'.")
        return df