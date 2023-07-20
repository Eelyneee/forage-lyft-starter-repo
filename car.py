from serviceable import Serviceable
from battery import Battery
from engine import Engine
from tires import Tires

class Car(Serviceable,Engine,Battery,Tires):
    def __init__(self, engine, battery,tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
