from Startup import Startup
from Shutdown import Shutdown
class Facade():
    @staticmethod
    def beginWork():
        print("Starting up")
        Startup().method()
    
    @staticmethod
    def shutdown():
        print("Beginning Shutdown")
        Shutdown().method()