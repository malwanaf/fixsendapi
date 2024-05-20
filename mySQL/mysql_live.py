import json
import requests
import time

# Function to send data to API
def send_data_to_api(data):
    url = 'http://192.168.1.113:3000/strikes'  # Change this URL if needed
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print('Data sent successfully')
        return True
    else:
        print('Failed to send data:', response.text)
        return False

# Function to read JSON data from file
def read_json_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to read sent strikes from file
def read_sent_strikes(filename):
    try:
        with open(filename, 'r') as file:
            sent_strikes = set(json.load(file))
    except FileNotFoundError:
        sent_strikes = set()
    return sent_strikes

# Function to write sent strikes to file
def write_sent_strikes(filename, sent_strikes):
    with open(filename, 'w') as file:
        json.dump(list(sent_strikes), file)

# Main function
def main():
    filename = 'data-new.json'  # Change this filename if needed
    sent_strikes_file = 'sent_strikes.json'  # Change this filename if needed

    sent_strikes = read_sent_strikes(sent_strikes_file)

    while True:
        try:
            data = read_json_data(filename)
            if data:
                strikes_to_send = {k: v for k, v in data.items() if v['id'] not in sent_strikes}
                for key, strike_data in strikes_to_send.items():
                    if send_data_to_api(strike_data):
                        sent_strikes.add(strike_data['id'])
                # We don't remove sent strikes from the file
            else:
                print('No new data found in file')
            time.sleep(5)  # Adjust this delay as per your requirement
        except Exception as e:
            print('Error:', e)
            time.sleep(5)  # Wait before trying again

        # Write sent strikes to file
        write_sent_strikes(sent_strikes_file, sent_strikes)

if __name__ == "__main__":
    main()
