import random
class Sensors:
    def checkVoltage() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Sensors: Voltage insufficient"
        else:
            return "Sensors: Voltage level stable"
        
    def checkPower() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Sensors: Power supply temperature: 3051 degrees celsius"
        else:
            return "Sensors: Power supply temperature: 40 degrees celsius"
        
    def checkVideo() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Sensors: Video card temperature: 1005 degrees celsius"
        else:
            return "Sensors: Video card temperature: 35 degrees celsius"
        
    def checkRAM() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Sensors: RAM temperature: -130 degrees celsius"
        else:
            return "Sensors: RAM temperature: 37 degrees celsius"
        
    def checkAll() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Sensors: Systems temperatures unstable"
        else:
            return "Sensors: Systems temperatures stable"