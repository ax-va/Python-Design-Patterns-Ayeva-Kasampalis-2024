"""
The *Dependency Injection* pattern involves passing the dependencies of a class as external entities
rather than creating them within the class, which promotes loose coupling, modularity, and testability.
It is applicable not only in testing scenarios but also in general software design.
"""
from typing import Protocol


# Example:
# A `WeatherService` class depends on a `WeatherApiClientInterface` interface to fetch weather data.
# We will inject a mock version of this API client.

# Define the interface any weather API client implementation should conform to
class WeatherApiClient(Protocol):
    def fetch_weather(self, location: str):
        """Fetch weather data for a given location"""
        ...


# implementation of the interface
class RealWeatherApiClient:
    def fetch_weather(self, location: str):
        # Perform a call to a weather service ...
        return f"Real weather data for {location}"


class WeatherService:
    def __init__(self, weather_api: WeatherApiClient):
        self.weather_api = weather_api

    def get_weather(self, location: str):
        return self.weather_api.fetch_weather(location)


if __name__ == "__main__":
    ws = WeatherService(RealWeatherApiClient())
    print(ws.get_weather("Paris"))
    # Real weather data for Paris
