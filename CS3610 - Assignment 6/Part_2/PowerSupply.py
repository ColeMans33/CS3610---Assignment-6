import random
class PowerSupply:
    def apply() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Power Supply: Power application failed"
        else:
            return "Power Supply: Power applied successfully"
        
    def checkVideo() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Power Supply: Video card not detected"
        else:
            return "Power Supply: Video card power supplied successfully"
        
    def supplyRAM() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Power Supply: RAM not detected"
        else:
            return "Power Supply: RAM power applied successfully"
        
    def supplyDisc() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Power Supply: Optical disc reader not detected"
        else:
            return "Power Supply: Optical disc reader power applied successfully"
        
    def supplyHDD() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Power Supply: HDD not detected"
        else:
            return "Power Supply: HDD power applied successfully"
        
    def stopVideo() -> str:
        return "Power Supply: Video card power cut"

    def stopDisc() -> str:
        return "Power Supply: Optical disc power cut"
    
    def stopRAM() -> str:
        return "Power Supply: RAM power cut"
    
    def stopHDD() -> str:
        return "Power Supply: HDD power cut"
    
    def shutdown() -> str:
        return "Power Supply: Shutting down"