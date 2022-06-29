import datetime
from Battery import Battery
class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today()
    
    def needs_service(self):
        return super().needs_service()