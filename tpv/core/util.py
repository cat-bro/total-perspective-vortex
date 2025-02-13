import os
import yaml

import requests


def load_yaml_from_url_or_path(url_or_path: str):
    if os.path.isfile(url_or_path):
        with open(url_or_path, 'r') as f:
            return yaml.safe_load(f)
    else:
        with requests.get(url_or_path) as r:
            return yaml.safe_load(r.content)
