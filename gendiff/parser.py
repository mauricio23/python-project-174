import json
import yaml
import os

def parse(ruta):
    _, ext = os.path.splitext(ruta)
    ext = ext.lower()

    with open(ruta, 'r', encoding='utf-8') as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Extensión no soportada: {ext}")