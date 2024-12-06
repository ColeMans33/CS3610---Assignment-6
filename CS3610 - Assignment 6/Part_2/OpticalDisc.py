import random
class OpticalDisc:
    def startup() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Optical disc reader: Startup failed"
        else:
            return "Optical disc reader: Startup successful"
        
    def checkDisc() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "Optical disc reader: Disc presence not detected"
        else:
            return "Optical disc reader: Disc presence detected"
        
    def originalPosition() -> str:
        return "Optical disc reader: Returned to original position"