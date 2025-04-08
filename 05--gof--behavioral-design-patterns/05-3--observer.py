"""
Observer

The *Observer* pattern describes a *publish-subscribe relationship* between the *publisher*,
also known as the *subject* or *observable* (or *event* in event-driven systems),
and the subscribers, also known as the *observers* (or *listeners* in event-driven systems).
The subject notifies the subscribers of any state changes, typically by calling one of their methods.
The observers can be dynamically attached to or removed from observing the subject at runtime.

Example:
- weather station as the subject;
- devices and applications as the observers,
e.g., smartphones, tablets, weather apps, and so on.
"""

# common observer
class WeatherObserver:
    # The weather station calls `update` when notifying about changes
    def update(self, **weather_data):
        print(
            f"\tTemperature: {weather_data.get('temperature')}°C, "
            f"Humidity: {weather_data.get('humidity')}%, "
            f"Pressure: {weather_data.get('pressure')}hPa"
        )

# subject
class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_weather_data(self, **weather_data):
        # notify observers
        for observer in self.observers:
            observer.update(**weather_data)


# real observers

class DisplayDevice(WeatherObserver):
    def __init__(self, name):
        self.name = name

    def update(self, **weather_data):
        print(f"Display device: {self.name}")
        super().update(**weather_data)


class WeatherApp(WeatherObserver):
    def __init__(self, name):
        self.name = name

    def update(self, **weather_data):
        print(f"Weather app: {self.name}")
        super().update(**weather_data)


if __name__ == "__main__":
    weather_station = WeatherStation()

    display1 = DisplayDevice("Living Room")
    display2 = DisplayDevice("Bedroom")
    app1 = WeatherApp("Mobile App Alex")
    app2 = WeatherApp("Mobile App Tatiana")

    weather_station.add_observer(display1)
    weather_station.add_observer(display2)
    weather_station.add_observer(app1)
    weather_station.add_observer(app2)

    weather_station.set_weather_data(temperature=25.5, humidity=60, pressure=1013.2)
    # Display device: Living Room
    #     Temperature: 25.5°C, Humidity: 60%, Pressure: 1013.2hPa
    # Display device: Bedroom
    #     Temperature: 25.5°C, Humidity: 60%, Pressure: 1013.2hPa
    # Weather app: Mobile App Alex
    #     Temperature: 25.5°C, Humidity: 60%, Pressure: 1013.2hPa
    # Weather app: Mobile App Tatiana
    #     Temperature: 25.5°C, Humidity: 60%, Pressure: 1013.2hPa
    weather_station.set_weather_data(temperature=26.0, humidity=58, pressure=1012.8)
    # Display device: Living Room
    #     Temperature: 26.0°C, Humidity: 58%, Pressure: 1012.8hPa
    # Display device: Bedroom
    #     Temperature: 26.0°C, Humidity: 58%, Pressure: 1012.8hPa
    # Weather app: Mobile App Alex
    #     Temperature: 26.0°C, Humidity: 58%, Pressure: 1012.8hPa
    # Weather app: Mobile App Tatiana
    #     Temperature: 26.0°C, Humidity: 58%, Pressure: 1012.8hPa
    weather_station.remove_observer(app2)
    weather_station.set_weather_data(temperature=27.2, humidity=55, pressure=1012.5)
    # Display device: Living Room
    #     Temperature: 27.2°C, Humidity: 55%, Pressure: 1012.5hPa
    # Display device: Bedroom
    #     Temperature: 27.2°C, Humidity: 55%, Pressure: 1012.5hPa
    # Weather app: Mobile App Alex
    #     Temperature: 27.2°C, Humidity: 55%, Pressure: 1012.5hPa
