import json
import requests
import os
import time

def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'.")
        return {}

def send_to_api(data):
    api_endpoint = 'https://lddb-51b02-default-rtdb.asia-southeast1.firebasedatabase.app/db/raspy.json?auth=rS3XrS4WifKlKwXG0CrYa9hdslqifgZAB6wXAVMo'
    try:
        response = requests.post(api_endpoint, json=data)
        response.raise_for_status()
        print("Data sent successfully.")
        return True
    except requests.RequestException as e:
        print(f"Failed to send data: {e}")
        return False

def load_sent_entries(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading sent entries from '{filename}': {e}")
    return []

def save_sent_entries(entries, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(entries, f)
        print(f"Sent entries saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving sent entries to '{filename}': {e}")

def main():
    filename = "data2.json"
    sent_entries_file = "sent_entries.json"

    while True:
        data = read_json_file(filename)
        if data:
            sent_entries = load_sent_entries(sent_entries_file)

            new_entries = []
            for entry_key, entry_value in data.items():
                entry_id = entry_value.get('id')
                if entry_id and entry_id not in sent_entries:
                    new_entries.append(entry_id)

            if new_entries:
                # Send new entries to the API
                send_data = {'ids': new_entries}  # Assuming the API expects a list of IDs
                if send_to_api(send_data):
                    # Update sent entries
                    sent_entries.extend(new_entries)
                    save_sent_entries(sent_entries, sent_entries_file)

        time.sleep(1)

if __name__ == "__main__":
    main()
