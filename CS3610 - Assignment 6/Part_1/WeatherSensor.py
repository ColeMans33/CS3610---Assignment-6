import WeatherForecastInterface

#legacy service
class WeatherSensor():
    def getBinaryData(self):
        tempature = "01010111" #crazy weather we're having
        print("[Sensor] ", end='')
        print(f"Binary weather data: {tempature}")
        return tempature
