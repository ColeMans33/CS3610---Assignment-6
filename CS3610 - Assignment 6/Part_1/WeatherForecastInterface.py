from abc import ABC, abstractmethod

class WeatherForecastInterface(ABC):

    @abstractmethod
    def displayData(self):
        pass