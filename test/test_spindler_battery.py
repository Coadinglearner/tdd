import unittest
from datetime import datetime, timedelta
from car_factory import CarFactory

class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        self.factory = CarFactory()

    def test_spindler_battery_needs_service_after_three_years(self):
        last_service_date = datetime(2022, 1, 15)
        spindler_battery = self.factory.create_spindler_battery(last_service_date)
        threshold_date = last_service_date.replace(year=last_service_date.year + 3)
        self.assertEqual(spindler_battery.next_service_date(), threshold_date)

if __name__ == '__main__':
    unittest.main()
