from typing import List

from hypergol import BaseData

from data_models.attribute import Attribute
from data_models.hour import Hour


class Business(BaseData):

    def __init__(self, business_id: str, name: str, address: str, city: str, state: str, postal_code: str, latitude: float, longitude: float, stars: float, review_count: int, is_open: int, attributes: List[Attribute], categories: List[str], hours: List[Hour]):
        self.business_id = business_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
        self.stars = stars
        self.review_count = review_count
        self.is_open = is_open
        self.attributes = attributes
        self.categories = categories
        self.hours = hours

    def get_id(self):
        return (self.business_id, )

    def to_data(self):
        data = self.__dict__.copy()
        data['attributes'] = [v.to_data() for v in data['attributes']]
        data['hours'] = [v.to_data() for v in data['hours']]
        return data

    @classmethod
    def from_data(cls, data):
        data['attributes'] = [Attribute.from_data(v) for v in data['attributes']]
        data['hours'] = [Hour.from_data(v) for v in data['hours']]
        return cls(**data)
