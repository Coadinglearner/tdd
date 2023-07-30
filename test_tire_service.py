import unittest
from car_factory import CarFactory

class TestTireService(unittest.TestCase):
    def setUp(self):
        self.factory = CarFactory()

    def test_carrigan_tire_needs_service(self):
        tire_wear = [0.1, 0.8, 0.3, 0.6]
        carrigan_tire = self.factory.create_carrigan_tire(tire_wear)
        self.assertTrue(carrigan_tire.needs_service())

    def test_carrigan_tire_does_not_need_service(self):
        tire_wear = [0.1, 0.8, 0.3, 0.5]
        carrigan_tire = self.factory.create_carrigan_tire(tire_wear)
        self.assertFalse(carrigan_tire.needs_service())

    def test_octoprime_tire_needs_service(self):
        tire_wear = [0.9, 0.7, 1.0, 0.5]
        octoprime_tire = self.factory.create_octoprime_tire(tire_wear)
        self.assertTrue(octoprime_tire.needs_service())

    def test_octoprime_tire_does_not_need_service(self):
        tire_wear = [0.8, 0.7, 1.0, 0.5]
        octoprime_tire = self.factory.create_octoprime_tire(tire_wear)
        self.assertFalse(octoprime_tire.needs_service())

if __name__ == '__main__':
    unittest.main()
