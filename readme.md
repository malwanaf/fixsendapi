# JSON Data Sender

This Python script monitors changes in a JSON file and sends new data to an API endpoint. It keeps track of the entries that have been successfully sent to the API to avoid resending them upon restart.

## Features

- Monitors changes in a JSON file.
- Sends new data to an API endpoint.
- Keeps track of sent entries to avoid resending them upon restart.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

## Installation

You can install the required dependencies using pip. Or use a virtual environment for the installation:

1. Clone the repository:

```bash
git clone https://github.com/malwanaf/fixsendapi.git
cd fixsendapi
```

2. Using python venv (optional)

```bash
python3 -m venv env_name
source .venv/env_name/bin/activate
```

3. Install requests library on venv

```bash
.venv/env_name/bin/pip install requests
```

## Usage

#### Replace the following variables in the script according to your setup:

1. json_file_path: Path to the JSON file to monitor.

2. api_url: URL of the API endpoint to send the data.

3. sent_entries_file: Path to the file storing the IDs of sent entries.

4. Go to the file location, and run the app:

```bash
python main.py
```