from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.hour import Hour


class TestHour(TestCase):

    def __init__(self, methodName):
        super(TestHour, self).__init__(methodName=methodName)
        self.hour = Hour(Monday='', Tuesday='', Wednesday='', Thursday='', Friday='', Saturday='', Sunday='')

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_hour_test_get_hash_id(self):
        self.assertEqual(self.hour.test_get_hash_id(), True)

    def test_hour_test_to_data(self):
        self.assertEqual(self.hour.test_to_data(), True)

    def test_hour_test_from_data(self):
        self.assertEqual(self.hour.test_from_data(), True)
