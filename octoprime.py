from tyres.tyre import tyre


class octoprime(tyre):
    tyre_wear = []
    def __init__(self, tyre_wear):
        for i in tyre_wear:
            self.tyre_wear.append(i)
    
    def needs_service(self):
        for i in self.tyre_wear:
            sum += i
        if sum >= 3:
            return True
        else:
            return False