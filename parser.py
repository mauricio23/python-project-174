import json
import yaml

def parse(data, fmt):
    if fmt == 'json':
        return json.loads(data)
    elif fmt in ['yml', 'yaml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Formato no soportado: {fmt}")