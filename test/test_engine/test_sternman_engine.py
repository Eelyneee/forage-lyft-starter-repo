import unittest

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_loght_on = True
        engine = SternmanEngine(warning_loght_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()