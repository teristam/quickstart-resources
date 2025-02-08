from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os 

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("weather")
# Constants updated for Open-Meteo API
OPENMETEO_API_BASE = "https://api.open-meteo.com/v1"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(location: str) -> str:
    """Get weather alerts for a location using Open-Meteo API.

    Uses Open-Meteo's geocoding to obtain coordinates, then fetches alerts.
    """
    # Geolocate location using Open-Meteo Geocoding API (global search)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
    geo_data = await make_nws_request(geo_url)
    if not geo_data or "results" not in geo_data or not geo_data["results"]:
        return "Unable to geolocate the location."
    geo_result = geo_data["results"][0]
    lat = geo_result.get("latitude")
    lon = geo_result.get("longitude")
    loc_name = geo_result.get("name", location)
    country = geo_result.get("country", "")
    if lat is None or lon is None:
        return "Invalid geolocation data."
    
    # Fetch alerts using Open-Meteo Alerts endpoint
    alerts_url = f"{OPENMETEO_API_BASE}/alerts?latitude={lat}&longitude={lon}&timezone=auto"
    alert_data = await make_nws_request(alerts_url)
    if not alert_data or "alerts" not in alert_data or not alert_data["alerts"]:
        return f"No active alerts for {loc_name}, {country}."
    
    formatted_alerts = [f"Alerts for {loc_name}, {country}:"]
    for alert in alert_data["alerts"]:
        msg = f"""
Sender: {alert.get('sender', 'Unknown')}
Event: {alert.get('event', 'Unknown')}
Start: {alert.get('start', 'N/A')}
End: {alert.get('end', 'N/A')}
Description: {alert.get('description', 'No description')}
"""
        formatted_alerts.append(msg)
    return "\n---\n".join(formatted_alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location using Open-Meteo API.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.
    """
    forecast_url = (f"{OPENMETEO_API_BASE}/forecast?latitude={latitude}&longitude={longitude}"
                    "&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto")
    forecast_data = await make_nws_request(forecast_url)
    if not forecast_data or "daily" not in forecast_data:
        return "Unable to fetch forecast data for this location."
    
    daily = forecast_data["daily"]
    times = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    weathercodes = daily.get("weathercode", [])
    formatted_forecasts = []
    
    for i in range(min(5, len(times))):
        forecast = f"""
Date: {times[i]}
Temperature: Max {max_temps[i]}°F, Min {min_temps[i]}°F
Weather Code: {weathercodes[i]}
"""
        formatted_forecasts.append(forecast)
    return "\n---\n".join(formatted_forecasts)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
