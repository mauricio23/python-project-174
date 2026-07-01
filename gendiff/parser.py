import json
import yaml
import os

def parse(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    with open(file_path, 'r', encoding='utf-8') as f:
        if ext == '.json':
            return json.load(f)  
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Extensión no soportada: {ext}")