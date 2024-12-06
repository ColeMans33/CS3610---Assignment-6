class WeatherController:
    def __init__(self, sensor):
        self.sensor = sensor

    def display_data(self):
        binary_data = self.sensor.get_binary_data()
        print(f"Displaying binary weather data: {binary_data.hex()}")