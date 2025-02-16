from flask import Blueprint, render_template, jsonify, current_app
from datetime import datetime
from utils import load_timestamps, save_timestamps

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/timestamps", methods=["GET"])
def get_timestamps():
    """Return timestamps in the correct order (most recent first)."""
    timestamps = load_timestamps()
    return jsonify(list(timestamps))  

@routes.route("/add_timestamp", methods=["POST"])
def add_timestamp():
    """Add a new timestamp and enforce queue structure."""
    timestamps = load_timestamps()
    timestamps.append(datetime.now().isoformat())  

    save_timestamps(timestamps)
    return jsonify({"message": "Timestamp added!", "count": len(timestamps)})
