import random
class HDD:
    def launch() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "HDD: Launch failed"
        else:
            return "HDD: Launched successfully"
        
    def checkBoot() -> str:
        num = random.randint(0, 10)
        if (num == 0):
            return "HDD: Boot sector not found"
        else:
            return "HDD: Boot sector found"
        
    def stop() -> str:
        return "HDD: Shutting down"