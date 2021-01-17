from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.review_document import ReviewDocument


class TestReviewDocument(TestCase):

    def __init__(self, methodName):
        super(TestReviewDocument, self).__init__(methodName=methodName)
        self.reviewDocument = ReviewDocument(review_id='', user_id='', business_id='', stars=0.0, useful=0, funny=0, cool=0, text='', date='', sentences=None)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_review_document_test_get_hash_id(self):
        self.assertEqual(self.reviewDocument.test_get_hash_id(), True)

    def test_review_document_test_to_data(self):
        self.assertEqual(self.reviewDocument.test_to_data(), True)

    def test_review_document_test_from_data(self):
        self.assertEqual(self.reviewDocument.test_from_data(), True)
