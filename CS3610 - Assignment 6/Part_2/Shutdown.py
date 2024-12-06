from Videocard import Videocard
from RAM import RAM
from HDD import HDD
from OpticalDisc import OpticalDisc
from PowerSupply import PowerSupply
from Sensors import Sensors

class Shutdown:
    @staticmethod
    def method():
        print(HDD.stop())
        print(RAM.clear())
        print(RAM.workingMemory())
        print(Videocard.farewell())
        print(OpticalDisc.originalPosition())
        print(PowerSupply.stopVideo())
        print(PowerSupply.stopRAM())
        print(PowerSupply.stopDisc())
        print(PowerSupply.stopHDD())
        print(Sensors.checkVoltage())
        print(PowerSupply.shutdown())
