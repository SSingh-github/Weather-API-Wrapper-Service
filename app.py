from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv
import redis
import json  # To handle JSON serialization/deserialization

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
API_KEY = os.getenv("API_KEY")

# Connect to Redis
redis_cache = redis.Redis(
    host='redis-18856.c124.us-central1-1.gce.redns.redis-cloud.com',
    port=18856,
    decode_responses=True,  # Ensures Redis returns strings instead of bytes
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
)

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get query parameters
    location = request.args.get('location')   
    date1 = request.args.get('date1')        
    date2 = request.args.get('date2')        

    # Validate required parameters
    if not location or not date1 or not date2:
        return jsonify({"error": "Missing required query parameters: location, date1, and/or date2"}), 400

    # Generate Redis key
    cache_key = f"{location}:{date1}:{date2}"

    # Check if data is in Redis
    cached_data = redis_cache.get(cache_key)
    if cached_data:
        # Return cached data if it exists
        print("got the data from redis")
        return jsonify(json.loads(cached_data))

    # Construct the API URL
    url = f"{BASE_URL}/{location}/{date1}/{date2}?key={API_KEY}"

    try:
        # Fetch data from external API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()      # Parse the JSON response

        # Store the data in Redis (set with an expiration time, e.g., 1 day)
        redis_cache.setex(cache_key, 86400, json.dumps(data))  # Expires after 86400 seconds (1 day)

        # Return the fetched data
        print("got the data from api")
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
