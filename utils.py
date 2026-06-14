import json
import os

def load_data(filepath):
    """
    Load data from a JSON file.
    Returns empty list if file doesn't exist.
    """
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(filepath, data):
    """
    Save Python data to JSON file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


