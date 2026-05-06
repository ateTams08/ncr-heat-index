import openmeteo_requests
import pandas as pd
import requests_cache
import gspread
import os
import json
from retry_requests import retry
from google.oauth2.service_account import Credentials

# --- 1. SETUP & CITY MAPPING ---
SERVICE_ACCOUNT_FILE = 'service-account.json'
SHEET_TITLE = "Manila Weather Data"

CITY_NAMES = [
    "Manila", "Quezon City", "Caloocan North", 
    "Caloocan South", "Valenzuela", "Malabon", "Navotas", 
    "Marikina", "Pasig", "Taguig", "Makati", "Pasay", 
    "Parañaque", "Las Piñas", "Muntinlupa", "San Juan", 
    "Mandaluyong", "Pateros"
]

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": [
        14.5995, 14.6500, 14.7500, # Manila, QC, Caloocan N
        14.6500, 14.7000, 14.6600, # Caloocan S, Valenzuela, Malabon
        14.6667, 14.6500, 14.5605, # Navotas, Marikina, Pasig
        14.5200, 14.5566, 14.5500, # Taguig, Makati, Pasay
        14.5008, 14.4500, 14.3854, # Parañaque, Las Piñas, Muntinlupa
        14.6040, 14.5800, 14.5448  # San Juan, Mandaluyong, Pateros
    ],
    "longitude": [
        120.9842, 121.0475, 121.0500, # Manila, QC, Caloocan N
        120.9700, 120.9800, 120.9600, # Caloocan S, Valenzuela, Malabon
        120.9417, 121.1000, 121.0765, # Navotas, Marikina, Pasig
        121.0500, 121.0234, 121.0000, # Taguig, Makati, Pasay
        120.9915, 120.9800, 121.0290, # Parañaque, Las Piñas, Muntinlupa
        121.0300, 121.0300, 121.0671  # San Juan, Mandaluyong, Pateros
    ],
    "hourly": ["temperature_2m", "relative_humidity_2m", "apparent_temperature"],
    "timezone": "Asia/Manila",
    "past_days": 7,
    "forecast_days": 14,
}

print(f"Fetching data for {len(CITY_NAMES)} locations ...")
responses = openmeteo.weather_api(url, params=params)

all_locations_data = []

# --- 2. THE LOOP ---
for i, response in enumerate(responses):
    hourly = response.Hourly()

    city_label = CITY_NAMES[i] if i < len(CITY_NAMES) else f"Coord_{i}"import openmeteo_requests
import pandas as pd
import requests_cache
import gspread
import os
import json
from retry_requests import retry
from google.oauth2.service_account import Credentials

# --- 1. SETUP & CITY MAPPING ---
SHEET_TITLE = "Manila Weather Data"

CITY_NAMES = [
    "Manila", "Quezon City", "Caloocan North",
    "Caloocan South", "Valenzuela", "Malabon", "Navotas",
    "Marikina", "Pasig", "Taguig", "Makati", "Pasay",
    "Parañaque", "Las Piñas", "Muntinlupa", "San Juan",
    "Mandaluyong", "Pateros"
]

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": [
        14.5995, 14.6500, 14.7500,
        14.6500, 14.7000, 14.6600,
        14.6667, 14.6500, 14.5605,
        14.5200, 14.5566, 14.5500,
        14.5008, 14.4500, 14.3854,
        14.6040, 14.5800, 14.5448
    ],
    "longitude": [
        120.9842, 121.0475, 121.0500,
        120.9700, 120.9800, 120.9600,
        120.9417, 121.1000, 121.0765,
        121.0500, 121.0234, 121.0000,
        120.9915, 120.9800, 121.0290,
        121.0300, 121.0300, 121.0671
    ],
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature"
    ],
    "timezone": "Asia/Manila",
    "past_days": 7,
    "forecast_days": 14,
}

print(f"Fetching data for {len(CITY_NAMES)} locations ...")
responses = openmeteo.weather_api(url, params=params)

all_locations_data = []

# --- 2. PROCESS DATA ---
for i, response in enumerate(responses):
    hourly = response.Hourly()

    city_label = CITY_NAMES[i] if i < len(CITY_NAMES) else f"Coord_{i}"

    times = pd.date_range(
        start=pd.to_datetime(
            hourly.Time() + response.UtcOffsetSeconds(),
            unit="s",
            utc=True
        ),
        end=pd.to_datetime(
            hourly.TimeEnd() + response.UtcOffsetSeconds(),
            unit="s",
            utc=True
        ),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )

    df_loc = pd.DataFrame({
        "date": times.strftime('%Y-%m-%d %H:%M'),
        "city": city_label,
        "lat": params["latitude"][i],
        "lon": params["longitude"][i],
        "temp": hourly.Variables(0).ValuesAsNumpy(),
        "humidity": hourly.Variables(1).ValuesAsNumpy(),
        "apparent_temp": hourly.Variables(2).ValuesAsNumpy()
    })

    all_locations_data.append(df_loc)

final_df = pd.concat(all_locations_data, ignore_index=True)
final_df = final_df.fillna(0)

# --- 3. AUTHENTICATION (FIXED FOR GITHUB ACTIONS) ---
print("Authenticating using GitHub Secret...")

if not os.environ.get("GCP_SERVICE_ACCOUNT"):
    raise Exception("Missing GCP_SERVICE_ACCOUNT secret")

info = json.loads(os.environ["GCP_SERVICE_ACCOUNT"])

creds = Credentials.from_service_account_info(
    info,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

client = gspread.authorize(creds)

# --- 4. UPLOAD ---
try:
    ws = client.open(SHEET_TITLE).get_worksheet(0)

    data_to_send = [final_df.columns.values.tolist()] + final_df.values.tolist()

    ws.clear()
    ws.update(values=data_to_send, range_name='A1')

    print("Success! Your Metro Manila dashboard is updated.")

except Exception as e:
    print(f"Error: {e}")
