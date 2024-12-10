
import WeatherSensor
import WeatherXMLProcess

class WeatherXMLAdapter():
    def __init__(self, binarySensor: WeatherSensor):
        self.binarySensor = binarySensor #adaptee

    #wrapper
    def getXMLData(self):

        binaryData = self.binarySensor.getBinaryData()
        
        print("[Adapter] Converting Binary to XML")
        xmlData = binaryData
        print("[Adapter] Conversion Complete, analyzing....")

        #self.forecastXML.predictXMLData(xmlData) from old code - could be used to store xml

        return xmlData