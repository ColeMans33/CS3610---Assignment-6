import xml.etree.ElementTree as ET
import datetime

class WeatherUnderstanderAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def get_xml_data(self):

        binary_data = self.sensor.get_binary_data()
        
        
        timestamp = datetime.datetime.now()

        root = ET.Element("WeatherData")
        ET.SubElement(root, "Binary").text = binary_data.hex()
        ET.SubElement(root, "Timestamp").text = timestamp.strftime("%B")
        xml_data = ET.tostring(root, encoding='unicode')
        return xml_data