from Serviceable import serviceable
class Car(serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass
