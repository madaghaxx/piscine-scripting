import json
import os


def _search_credentials(data, credentials):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ("password", "secret") and key not in credentials:
                credentials[key] = value
            _search_credentials(value, credentials)
    elif isinstance(data, list):
        for item in data:
            _search_credentials(item, credentials)


def credentials_search():
    if not os.path.exists("logs.json"):
        return

    try:
        with open("logs.json", "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return

    credentials = {}
    _search_credentials(data, credentials)

    if credentials:
        with open("credentials.json", "w") as f:
            json.dump(credentials, f, indent=2)
    elif os.path.exists("credentials.json"):
        os.remove("credentials.json")
