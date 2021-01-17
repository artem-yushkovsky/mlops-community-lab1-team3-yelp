from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.business import Business


class TestBusiness(TestCase):

    def __init__(self, methodName):
        super(TestBusiness, self).__init__(methodName=methodName)
        self.business = Business(business_id='', name='', address='', city='', state='', postal_code='', latitude=0.0, longitude=0.0, stars=0.0, review_count=0, is_open=0, attributes=None, categories=['', ''], hours=None)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_business_test_get_hash_id(self):
        self.assertEqual(self.business.test_get_hash_id(), True)

    def test_business_test_to_data(self):
        self.assertEqual(self.business.test_to_data(), True)

    def test_business_test_from_data(self):
        self.assertEqual(self.business.test_from_data(), True)
