from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.attribute import Attribute


class TestAttribute(TestCase):

    def __init__(self, methodName):
        super(TestAttribute, self).__init__(methodName=methodName)
        self.attribute = Attribute(BusinessAcceptsCreditCards='', BikeParking='', GoodForKids='', BusinessParking='', ByAppointmentOnly='', RestaurantsPriceRange2='', DogsAllowed='', WiFi='', RestaurantsAttire='', RestaurantsTakeOut='', NoiseLevel='', RestaurantsReservations='', RestaurantsGoodForGroups='', HasTV='', Alcohol='', RestaurantsDelivery='', OutdoorSeating='', Caters='', WheelchairAccessible='', AcceptsInsurance='', RestaurantsTableService='', Ambience='', GoodForMeal='', HappyHour='', BusinessAcceptsBitcoin='', BYOB='', Corkage='', GoodForDancing='', CoatCheck='', BestNights='', Music='', Smoking='', DietaryRestrictions='', DriveThru='', HairSpecializesIn='', BYOBCorkage='', AgesAllowed='', RestaurantsCounterService='', Open24Hours='')

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_attribute_test_get_hash_id(self):
        self.assertEqual(self.attribute.test_get_hash_id(), True)

    def test_attribute_test_to_data(self):
        self.assertEqual(self.attribute.test_to_data(), True)

    def test_attribute_test_from_data(self):
        self.assertEqual(self.attribute.test_from_data(), True)
