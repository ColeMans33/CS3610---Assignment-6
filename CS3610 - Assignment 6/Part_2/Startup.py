from Videocard import Videocard
from RAM import RAM
from HDD import HDD
from OpticalDisc import OpticalDisc
from PowerSupply import PowerSupply
from Sensors import Sensors


class Startup():
    @staticmethod
    def method():
        print(PowerSupply.apply())
        print(Sensors.checkVoltage())
        print(Sensors.checkPower())
        print(Sensors.checkVideo())
        print(PowerSupply.checkVideo())
        print(Videocard.launch())
        print(Videocard.checkMonitor())
        print(Sensors.checkRAM())
        print(PowerSupply.supplyRAM())
        print(RAM.launch())
        print(RAM.memoryAnalysis())
        print(Videocard.displayRAM())
        print(PowerSupply.supplyDisc())
        print(OpticalDisc.startup())
        print(OpticalDisc.checkDisc())
        print(Videocard.displayDisc())
        print(PowerSupply.supplyHDD())
        print(HDD.launch())
        print(HDD.checkBoot())
        print(Videocard.outputHD())
        print(Sensors.checkAll())

