from WeatherSensor import WeatherSensor
from WeatherXMLAdapter import WeatherXMLAdapter
from WeatherXMLProcess import WeatherXMLProcess


#Instance
sensor = WeatherSensor()

#Using adapter
adapter = WeatherXMLAdapter(sensor)
xmlData = adapter.getXMLData()

#Process the adapted data
WeatherXMLProcess().xmlProcessor.predictXMLData(xmlData)

