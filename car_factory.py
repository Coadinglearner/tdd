from datetime import datetime

class SpindlerBattery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def next_service_date(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 3)

class CarriganTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)

class OctoprimeTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
