import json
import os

def credentials_search():
    if not os.path.exists('logs.json'):
        return
    
    try:
        with open('logs.json', 'r') as f:
            data = json.load(f)
    except:
        return
    
    credentials = {}
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'password' or key == 'secret':
                credentials[key] = value
    
    if credentials:
        with open('credentials.json', 'w') as f:
            json.dump(credentials, f, indent=2)
