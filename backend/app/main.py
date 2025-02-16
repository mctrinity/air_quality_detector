from fastapi import FastAPI
import os
import requests
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # Load environment variables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

AQI_LEVELS = {
    1: "Good",
    2: "Fair",
    3: "Moderate",
    4: "Poor",
    5: "Very Poor"
}

@app.get("/")
def home():
    return {"message": "Welcome to the Air Quality API!"}

@app.get("/air-quality")
def get_air_quality(lat: float, lon: float):
    if not API_KEY:
        return {"error": "Missing API key. Please set it in the .env file."}
    
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        air_data = data["list"][0]

        formatted_data = {
            "location": {
                "latitude": lat,
                "longitude": lon
            },
            "aqi": air_data["main"]["aqi"],
            "aqi_description": AQI_LEVELS.get(air_data["main"]["aqi"], "Unknown"),
            "components": {
                "CO (Carbon Monoxide)": air_data["components"]["co"],
                "NO (Nitric Oxide)": air_data["components"]["no"],
                "NO2 (Nitrogen Dioxide)": air_data["components"]["no2"],
                "O3 (Ozone)": air_data["components"]["o3"],
                "SO2 (Sulfur Dioxide)": air_data["components"]["so2"],
                "PM2.5 (Fine Particulate Matter)": air_data["components"]["pm2_5"],
                "PM10 (Coarse Particulate Matter)": air_data["components"]["pm10"],
                "NH3 (Ammonia)": air_data["components"]["nh3"]
            },
            "timestamp": datetime.utcfromtimestamp(air_data["dt"]).strftime('%Y-%m-%d %H:%M:%S UTC')
        }

        return formatted_data

    return {"error": "Unable to fetch air quality data"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

