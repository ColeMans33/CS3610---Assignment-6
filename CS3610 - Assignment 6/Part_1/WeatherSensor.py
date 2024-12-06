import random

class WeatherSensor:
    def get_binary_data(self):
        tempature = random.randint(1,40) #crazy weather we're having
        return bytes(tempature)
