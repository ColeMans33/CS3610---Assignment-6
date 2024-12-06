from WeatherController import *
from WeatherSensor import *
from WeatherUnderstander import *
from WeatherUnderstanderAdapter import *


sensor = WeatherSensor()
app = WeatherController(sensor)
app.display_data()



adapter = WeatherUnderstanderAdapter(sensor)

#XML testing
third_party_library = WeatherUnderstander()
xml_data = adapter.get_xml_data()
third_party_library.process_xml_data(xml_data)
