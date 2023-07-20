import unittest
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_sensor_data = [0.8,0.7,0.9,0.8]
        tires = OctoprimeTires(tire_sensor_data)
        self.assertTrue(tires.needs_service())

    def test_need_service_false(self):
        tire_sensor_data = [0.1, 0.1, 0.1, 0.1]
        tires = OctoprimeTires(tire_sensor_data)
        self.assertFalse(tires.needs_service())