import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
DATA_FOLDER = os.getenv("DATA_FOLDER", os.path.join(BASE_DIR, "data"))

class Config:
    DATA_FILE = os.path.join(DATA_FOLDER, "timestamps.json")  
    MAX_ENTRIES = int(os.getenv("MAX_ENTRIES", 50))
