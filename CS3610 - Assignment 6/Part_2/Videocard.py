import random
class Videocard:
    def launch() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Video card: Launch failed"
        else:
            return "Video card: Launch successful"
        
    def checkMonitor() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Video card: Monitor connection not found"
        else:
            return "Video card: Monitor connection found"
        
    def displayRAM() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Video card: RAM not found"
        else:
            return "Video card: 16gb RAM found"
        
    def displayDisc() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Video card: Disc reader not found"
        else:
            return "Video card: Disc reader found"
        
    def outputHD() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Video card: Hard drive not found"
        else:
            return "Video card: 256GB Hard drive found"
        

    def farewell() -> str:
        return "Video card: Farewell"
