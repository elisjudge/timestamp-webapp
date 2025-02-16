import json
import os
import collections
from flask import current_app

def ensure_data_folder():
    """Ensure that the data folder exists before saving the file."""
    data_folder = os.path.dirname(current_app.config["DATA_FILE"])
    if not os.path.exists(data_folder):
        os.makedirs(data_folder, exist_ok=True)

def load_timestamps():
    """Load timestamps from the JSON file and ensure it's a queue."""
    data_file = current_app.config["DATA_FILE"]
    
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return collections.deque(data, maxlen=current_app.config["MAX_ENTRIES"])  # Use deque with max limit
    return collections.deque(maxlen=current_app.config["MAX_ENTRIES"])  # Return empty queue

def save_timestamps(timestamps):
    """Save timestamps to the JSON file."""
    ensure_data_folder()
    data_file = current_app.config["DATA_FILE"]
    
    with open(data_file, "w") as f:
        json.dump(list(timestamps), f, indent=4)  # Convert deque back to list for storage
