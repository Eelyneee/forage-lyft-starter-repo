import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_need_service_true(self):
        tire_sensor_data = [0.9,0.1,0.1,0.1]
        tires = CarriganTires(tire_sensor_data)
        self.assertTrue(tires.needs_service())

    def test_need_service_false(self):
        tire_sensor_data = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(tire_sensor_data)
        self.assertFalse(tires.needs_service())