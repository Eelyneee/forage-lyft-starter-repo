import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_services_true(self):
        current_date = date.fromisoformat("2023-07-20")
        last_service_date = date.fromisoformat("2020-03-23")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-07-20")
        last_service_date = date.fromisoformat("2020-06-23")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()