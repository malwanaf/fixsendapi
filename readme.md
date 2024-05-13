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

## Supported JSON Format

```bash
{
  "data0": {
    "id": 0,
    "time": "2024-04-27",
    "distance": 3,
    "intensity": 8
  },
  "data0": {
    "id": 0,
    "time": "2024-04-27",
    "distance": 3,
    "intensity": 8
  }
}

{"2024-05-13 09:38:18.239311": {"id": "72d77a8e-9cfb-4176-aeb3-95c84e7131c7", "time": "2024-05-13 09:38:18.239311", "distance": 1, "intensity": 28.643202002741848}, "2024-05-13 09:38:29.333593": {"id": "0e068658-a808-4645-8945-a2c2313cefd0", "time": "2024-05-13 09:38:29.333593", "distance": 1, "intensity": 25.521368540263456}, "2024-05-13 09:38:36.217351": {"id": "2d51a39b-0c1e-4fd3-b8e4-5ae28656ee67", "time": "2024-05-13 09:38:36.217351", "distance": 1, "intensity": 2.448173094116946}, "2024-05-13 09:38:36.946932": {"id": "eee61d06-1d9f-4507-9a02-59c456aeb53d", "time": "2024-05-13 09:38:36.946932", "distance": 1, "intensity": 0.0}, "2024-05-13 09:38:43.693600": {"id": "344849f7-df1a-4ea2-935d-0860e5fffc47", "time": "2024-05-13 09:38:43.693600", "distance": 1, "intensity": 7.8126005841330395}, "2024-05-13 09:38:56.604057": {"id": "65f3edd4-8989-4fb0-9f27-f675c49cc7c4", "time": "2024-05-13 09:38:56.604057", "distance": 1, "intensity": 15.625201168266079}, "2024-05-13 09:38:57.333955": {"id": "72c65bd1-0cc5-4dbb-9122-f8ae9af55114", "time": "2024-05-13 09:38:57.333955", "distance": 1, "intensity": 0.0}, "2024-05-13 09:38:58.062838": {"id": "4ce35df5-8bcf-42e3-855f-4932bbe59bac", "time": "2024-05-13 09:38:58.062838", "distance": 1, "intensity": 0.0}, "2024-05-13 09:38:58.777167": {"id": "92f67f6e-a414-4448-affd-52db89bb9c7c", "time": "2024-05-13 09:38:58.777167", "distance": 1, "intensity": 6.639446861775049}, "2024-05-13 09:39:47.638678": {"id": "b33a14cf-a171-43b1-968d-95625ecd13e6", "time": "2024-05-13 09:39:47.638678", "distance": 1, "intensity": 12.893783155510521}, "2024-05-13 09:39:48.348896": {"id": "ac2bb8e9-7e83-48b6-a8ff-312737e3f1e5", "time": "2024-05-13 09:39:48.348896", "distance": 1, "intensity": 0.0}, "2024-05-13 09:39:49.614243": {"id": "8a513bcf-3c4f-42c9-b5ee-5f016eda961a", "time": "2024-05-13 09:39:49.614243", "distance": 1, "intensity": 5.914704655182691}, "2024-05-13 09:40:01.604155": {"id": "e3a8c3ab-c1cd-4df8-b8c8-d94e3541a438", "time": "2024-05-13 09:40:01.604155", "distance": 1, "intensity": 1.9505871133098884}, "2024-05-13 09:40:02.307797": {"id": "0ba6311d-f00e-443c-b24e-70f7af3cdeaa", "time": "2024-05-13 09:40:02.307797", "distance": 1, "intensity": 1.1165285807951362}, "2024-05-13 09:40:03.429073": {"id": "80b39491-0c92-464e-917b-d485d5a0ca4c", "time": "2024-05-13 09:40:03.429073", "distance": 1, "intensity": 28.37932884305895}, "2024-05-13 09:40:20.677234": {"id": "d45a594d-d4cb-4e92-98e7-78a1b6f93250", "time": "2024-05-13 09:40:20.677234", "distance": 1, "intensity": 2.6654348214817905}, "2024-05-13 09:40:21.498564": {"id": "25902bd6-99f8-43f7-9ea6-c92ff33ea2b2", "time": "2024-05-13 09:40:21.498564", "distance": 1, "intensity": 4.037730225904512}, "2024-05-13 09:40:27.260896": {"id": "ac0b6ad9-50ad-447b-8883-235c9827b84a", "time": "2024-05-13 09:40:27.260896", "distance": 1, "intensity": 0.4980032186922573}, "2024-05-13 09:40:58.172713": {"id": "00703a67-719f-4fab-ad5a-b70fcb0c6082", "time": "2024-05-13 09:40:58.172713", "distance": 1, "intensity": 0.11444239136913632}, "2024-05-13 09:41:15.429224": {"id": "49f70bca-ae29-4733-9d2a-e5afc7236f9e", "time": "2024-05-13 09:41:15.429224", "distance": 1, "intensity": 29.348095607081124}, "2024-05-13 09:41:17.420890": {"id": "1e58c9e8-a98d-4a78-bdf7-516b8abe58aa", "time": "2024-05-13 09:41:17.420890", "distance": 1, "intensity": 0.0}, "2024-05-13 09:41:17.990051": {"id": "1c1efe82-f223-4c35-a244-4ac333f34e45", "time": "2024-05-13 09:41:17.990051", "distance": 1, "intensity": 3.6621565238123623}, "2024-05-13 09:41:19.098628": {"id": "41fd649b-a715-414a-b4cb-11b728a3fff7", "time": "2024-05-13 09:41:19.098628", "distance": 1, "intensity": 12.459796149490373}, "2024-05-13 09:41:21.118241": {"id": "6fb6f7b1-0099-44f0-b487-af05cfa331fb", "time": "2024-05-13 09:41:21.118241", "distance": 1, "intensity": 0.0}, "2024-05-13 09:41:22.513759": {"id": "2bcae674-5c04-4e15-917e-fa272cb820bf", "time": "2024-05-13 09:41:22.513759", "distance": 1, "intensity": 11.35340048876438}, "2024-05-13 09:41:25.593469": {"id": "486ebeed-5b31-4eb1-baeb-5ab849e7acd6", "time": "2024-05-13 09:41:25.593469", "distance": 1, "intensity": 19.31578947368421}, "2024-05-13 09:41:31.416872": {"id": "f21e7099-dc2d-4fbb-9fa1-86cf96bf9bfb", "time": "2024-05-13 09:41:31.416872", "distance": 1, "intensity": 3.9602431900816595}, "2024-05-13 09:41:35.457878": {"id": "97e4752a-e90c-40b7-aa58-5b91e0215e55", "time": "2024-05-13 09:41:35.457878", "distance": 1, "intensity": 1.2566012993979854}, "2024-05-13 09:41:41.571362": {"id": "f41b5d7e-a51c-4680-aa15-8a4f542d7de4", "time": "2024-05-13 09:41:41.571362", "distance": 1, "intensity": 1.2865828217202122}, "2024-05-13 09:41:49.914982": {"id": "5d911f20-6987-425e-b7c5-ab348318f78d", "time": "2024-05-13 09:41:49.914982", "distance": 1, "intensity": 0.0}, "2024-05-13 09:41:52.814140": {"id": "0ef7e076-88d1-4b5f-88d7-e0ad687f7b74", "time": "2024-05-13 09:41:52.814140", "distance": 1, "intensity": 0.6644215294748763}, "2024-05-13 09:41:58.402877": {"id": "aa1c1c16-6346-4be7-9f99-51dd0a193838", "time": "2024-05-13 09:41:58.402877", "distance": 1, "intensity": 0.0}, "2024-05-13 09:42:10.165993": {"id": "42f843ac-71c5-4c14-8e8f-a61283b5ac9c", "time": "2024-05-13 09:42:10.165993", "distance": 1, "intensity": 1.5598736365261965}, "2024-05-13 09:49:04.149988": {"id": "5a08b568-1703-4239-b1c7-4309f6bce33b", "time": "2024-05-13 09:49:04.149988", "distance": 6, "intensity": 10.4901949096978}, "2024-05-13 09:49:11.187318": {"id": "55c15b53-732e-48b2-85db-85a14026f4d8", "time": "2024-05-13 09:49:11.187318", "distance": 6, "intensity": 4.920486380163319}, "2024-05-13 09:49:53.032319": {"id": "9464134d-190a-41e5-86c9-5c24ec862b61", "time": "2024-05-13 09:49:53.032319", "distance": 6, "intensity": 6.2576145914048995}, "2024-05-13 09:50:09.727202": {"id": "de99a4d2-c596-41d6-84ed-399b98e62af0", "time": "2024-05-13 09:50:09.727202", "distance": 5, "intensity": 12.670978124813733}, "2024-05-13 09:52:13.658333": {"id": "f595c254-0302-4fe8-8406-bb30d55bc4c8", "time": "2024-05-13 09:52:13.658333", "distance": 6, "intensity": 7.736424867377958}, "2024-05-13 09:52:43.362978": {"id": "a55f6daa-9e19-4117-aa24-dd471a21ba8c", "time": "2024-05-13 09:52:43.362978", "distance": 5, "intensity": 10.955951600405317}, "2024-05-13 09:53:20.643770": {"id": "632c944f-777c-482c-9ec6-e4bd11bb5ba6", "time": "2024-05-13 09:53:20.643770", "distance": 5, "intensity": 5.5139774691542}, "2024-05-13 09:55:56.370477": {"id": "dcbabed7-e45c-4c7d-b807-35b5fafcf4a9", "time": "2024-05-13 09:55:56.370477", "distance": 1, "intensity": 22.00888120641354}, "2024-05-13 09:57:18.820262": {"id": "61bc0f1a-a0dc-4cd6-93dd-7db2c10280fa", "time": "2024-05-13 09:57:18.820262", "distance": 1, "intensity": 9.09364010252131}, "2024-05-13 09:59:01.225688": {"id": "99d7e447-374f-4369-b578-507882a162e5", "time": "2024-05-13 09:59:01.225688", "distance": 1, "intensity": 13.929069559516003}, "2024-05-13 10:02:15.008305": {"id": "ab8ef7eb-9604-4a52-904f-c90f0f536023", "time": "2024-05-13 10:02:15.008305", "distance": 1, "intensity": 12.567264707635454}, "2024-05-13 10:02:46.426471": {"id": "8ce24f98-e9da-4b89-9cad-322d4166519e", "time": "2024-05-13 10:02:46.426471", "distance": 1, "intensity": 9.317756452285867}, "2024-05-13 10:03:21.753719": {"id": "76be16e0-b000-4a60-84da-472e9a3aed0f", "time": "2024-05-13 10:03:21.753719", "distance": 1, "intensity": 12.456815878881802}, "2024-05-13 10:03:26.919245": {"id": "94012972-7c2b-4fcb-b458-431d14b43292", "time": "2024-05-13 10:03:26.919245", "distance": 1, "intensity": 4.19741312511176}}

```

