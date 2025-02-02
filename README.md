# Weather API Wrapper Service

![Badge](https://img.shields.io/badge/python-3.8%2B-blue)
![Badge](https://img.shields.io/badge/flask-2.0%2B-green)
![Badge](https://img.shields.io/badge/redis-in--memory%20cache-orange)

A lightweight Flask-based service that acts as a wrapper for a third-party weather API. This project integrates external APIs, implements caching using Redis for faster responses, and manages environment variables for secure configuration.

---

## About the Project

### Problem Solved
Fetching real-time weather data from external APIs can be slow and expensive due to rate limits and network latency. This project solves these issues by:
1. **Caching weather data**: Using Redis as an in-memory cache to store API responses, reducing the need for repeated API calls.
2. **Improving performance**: Serving cached data for repeated requests, ensuring faster response times.
3. **Simplifying integration**: Providing a single endpoint for clients to fetch weather data without worrying about third-party API complexities.

---

## Features
- **Third-party API Integration**: Fetches real-time weather data from Visual Crossing's Weather API.
- **Caching Strategy**: Uses Redis to cache weather data with a 12-hour expiration time.
- **Environment Variable Management**: Securely manages API keys and configuration using environment variables.
- **Lightweight and Scalable**: Built with Flask, making it easy to deploy and scale.

---

## Technologies and Skills Used
- **Backend Framework**: Flask (Python)
- **Caching**: Redis (in-memory data store)
- **API Integration**: Visual Crossing Weather API
- **Environment Management**: `python-dotenv` for managing environment variables
- **Other Tools**: Git, Docker (optional for containerization)

---

## APIs and Services Used
### 1. **Visual Crossing Weather API**
   - **Endpoint**: `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/`
   - **Usage**: Fetches real-time weather data based on the city code provided by the user.
   - **Authentication**: API key required (stored securely in environment variables).

### 2. **Redis Cache**
   - **Usage**: Stores weather data with a 12-hour expiration time to reduce API calls.
   - **Key**: City code provided by the user.
   - **Value**: Weather data fetched from the API.

---

## How It Works
1. The user sends a request to the service with a city code.
2. The service checks if the weather data for that city is already cached in Redis.
   - If cached, the service returns the cached data.
   - If not cached, the service fetches the data from the Visual Crossing API, stores it in Redis, and returns it to the user.
3. Cached data automatically expires after 12 hours, ensuring up-to-date information.

---

## Steps to Clone and Run the Project

### Prerequisites
- Python 3.8+
- Redis server (locally or via Docker)
- Visual Crossing Weather API key (sign up [here](https://www.visualcrossing.com/weather-api))

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/weather-api-wrapper.git
cd weather-api-wrapper
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup environment variables in .env file

