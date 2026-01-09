"""
Port Moresby Weather Data Fetcher

Fetches 20 years of historical weather data from Open-Meteo API
for Port Moresby, Papua New Guinea.

This data will be analyzed by the LJPW Autopoiesis Module.
"""

import json
import csv
from datetime import datetime
from pathlib import Path
import urllib.request
import urllib.error

# Port Moresby coordinates
LATITUDE = -9.4438
LONGITUDE = 147.1803

# Date range: 20 years (2006-01-01 to 2026-01-04)
START_DATE = "2006-01-01"
END_DATE = "2026-01-04"

# Output file
OUTPUT_DIR = Path(__file__).parent
OUTPUT_FILE = OUTPUT_DIR / "weather_data_port_moresby.csv"

# Open-Meteo Historical Weather API endpoint
BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

# Daily weather variables to fetch
DAILY_VARIABLES = [
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "precipitation_sum",
    "rain_sum",
    "relative_humidity_2m_max",
    "relative_humidity_2m_min",
    "relative_humidity_2m_mean",
    "wind_speed_10m_max",
    "wind_speed_10m_mean",
    "surface_pressure_mean",
    "shortwave_radiation_sum",
    "daylight_duration",
    "sunshine_duration",
]


def build_url() -> str:
    """Build the API URL with all parameters."""
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "daily": ",".join(DAILY_VARIABLES),
        "timezone": "Pacific/Port_Moresby",
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{BASE_URL}?{query}"


def fetch_data() -> dict:
    """Fetch weather data from Open-Meteo API."""
    url = build_url()
    print(f"Fetching data from Open-Meteo API...")
    print(f"Location: Port Moresby, Papua New Guinea ({LATITUDE}, {LONGITUDE})")
    print(f"Date range: {START_DATE} to {END_DATE}")
    print()
    
    try:
        with urllib.request.urlopen(url, timeout=60) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        raise
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        raise


def save_to_csv(data: dict) -> int:
    """Save weather data to CSV file. Returns number of records."""
    daily = data.get("daily", {})
    
    if not daily or "time" not in daily:
        print("ERROR: No daily data found in response")
        return 0
    
    dates = daily["time"]
    num_records = len(dates)
    
    # Prepare column names (date + all weather variables)
    columns = ["date"] + DAILY_VARIABLES
    
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        
        for i, date in enumerate(dates):
            row = [date]
            for var in DAILY_VARIABLES:
                value = daily.get(var, [None] * num_records)[i]
                row.append(value if value is not None else "")
            writer.writerow(row)
    
    return num_records


def print_summary(data: dict, num_records: int):
    """Print a summary of the fetched data."""
    daily = data.get("daily", {})
    
    print("=" * 60)
    print("PORT MORESBY WEATHER DATA - FETCH COMPLETE")
    print("=" * 60)
    print(f"Total records: {num_records:,} days")
    print(f"Date range: {START_DATE} to {END_DATE}")
    print(f"Output file: {OUTPUT_FILE}")
    print()
    
    # Print some basic stats
    if daily.get("temperature_2m_mean"):
        temps = [t for t in daily["temperature_2m_mean"] if t is not None]
        if temps:
            print(f"Temperature (mean):")
            print(f"  Min: {min(temps):.1f}°C")
            print(f"  Max: {max(temps):.1f}°C")
            print(f"  Avg: {sum(temps)/len(temps):.1f}°C")
    
    if daily.get("precipitation_sum"):
        precip = [p for p in daily["precipitation_sum"] if p is not None]
        if precip:
            print(f"\nPrecipitation:")
            print(f"  Total: {sum(precip):,.1f} mm")
            print(f"  Avg daily: {sum(precip)/len(precip):.1f} mm")
            print(f"  Max daily: {max(precip):.1f} mm")
    
    if daily.get("shortwave_radiation_sum"):
        solar = [s for s in daily["shortwave_radiation_sum"] if s is not None]
        if solar:
            print(f"\nSolar Radiation:")
            print(f"  Avg daily: {sum(solar)/len(solar):.1f} MJ/m²")
            print(f"  Max daily: {max(solar):.1f} MJ/m²")
    
    print()
    print("Data ready for LJPW analysis!")
    print("=" * 60)


def main():
    """Main entry point."""
    print()
    print("=" * 60)
    print("  PORT MORESBY WEATHER DATA FETCHER")
    print("  For LJPW Autopoiesis Module Analysis")
    print("=" * 60)
    print()
    
    try:
        # Fetch data
        data = fetch_data()
        
        # Save to CSV
        num_records = save_to_csv(data)
        
        if num_records > 0:
            print_summary(data, num_records)
        else:
            print("ERROR: No data was saved")
            
    except Exception as e:
        print(f"\nERROR: {e}")
        raise


if __name__ == "__main__":
    main()
