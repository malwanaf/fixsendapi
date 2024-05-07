import requests
import json
import time
import os

def load_json_data(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

def post_json_to_api(json_data, api_url):
    try:
        response = requests.post(api_url, json=json_data)
        if response.status_code == 200:
            print("Data successfully posted to API")
            return True
        else:
            print("Failed to post data to API. Status code:", response.status_code)
            print("Response:", response.text)
            return False
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)
        return False

def load_sent_entries(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_sent_entries(entries, filename):
    with open(filename, 'w') as file:
        json.dump(entries, file)

def get_file_size(file_path):
    return os.path.getsize(file_path)

if __name__ == "__main__":

    # Add the json file
    json_file_path = './data-example.json'

    # Change API_URL
    api_url = 'https://lightningdetectorbmkg-default-rtdb.asia-southeast1.firebasedatabase.app/ld/raspy/data.json?auth=ZZHqaBLfrb8u0ULLoCfHfsH0sHJVtASoAGilrbsV'

    sent_entries_file = './sent_entries.json'

    # Load the IDs of previously sent entries
    sent_entries = load_sent_entries(sent_entries_file)

    while True:
        # Load the updated data
        current_data = load_json_data(json_file_path)

        # Compare current data with the previously sent data
        for entry_id, entry in current_data.items():
            if entry_id not in sent_entries:
                if post_json_to_api({entry_id: entry}, api_url):
                    sent_entries.append(entry_id)

        # Save the IDs of the newly sent entries
        save_sent_entries(sent_entries, sent_entries_file)

        time.sleep(1)  
