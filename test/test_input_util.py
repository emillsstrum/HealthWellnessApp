from unittest import TestCase
from datetime import date
from utils.input_util import *

class TestInputUtil(TestCase):
    # test cases for get_int()
    def test_get_int_valid_value(self):
        self.assertEqual(get_int("5"), 5)

    def test_get_int_invalid_value(self):
        self.assertIsNone(get_int("five"))

    # test cases for get_float()
    def test_get_float_valid_value(self):
        self.assertEqual(get_float("5.5"), 5.5)

    def test_get_float_invalid_value(self):
        self.assertIsNone(get_float("abc"))

    # test cases for get_int_range()
    def test_get_int_range_value_in_range(self):
        self.assertEqual(get_int_range(3, 1, 5), 3)

    def test_get_int_range_value_outside_range(self):
        self.assertIsNone(get_int_range(6, 1, 5))

    # test cases for get_date()
    def test_get_date_valid_date(self):
        self.assertEqual(get_date("04/12/2026"), date(2026, 4, 12))

    def test_get_date_invalid_year_length(self):
        self.assertIsNone(get_date("04/12/26"))

    def test_get_date_invalid_month_length(self):
        self.assertIsNone(get_date("4/12/2026"))

    def test_get_date_invalid_format(self):
        self.assertIsNone(get_date("2025/04/12"))

    def test_get_date_invalid_separator(self):
        self.assertIsNone(get_date("04-12-2026"))

    def test_get_date_invalid_data(self):
        self.assertIsNone(get_date("mm/dd/yyyy"))
