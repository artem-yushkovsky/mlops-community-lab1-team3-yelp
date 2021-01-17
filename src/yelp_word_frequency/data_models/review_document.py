from typing import List

from hypergol import BaseData

from data_models.sentence import Sentence


class ReviewDocument(BaseData):

    def __init__(self, review_id: str, user_id: str, business_id: str, stars: float, useful: int, funny: int, cool: int, text: str, date: str, sentences: List[Sentence], categories: List[str]):
        self.review_id = review_id
        self.user_id = user_id
        self.business_id = business_id
        self.stars = stars
        self.useful = useful
        self.funny = funny
        self.cool = cool
        self.text = text
        self.date = date
        self.sentences = sentences
        self.categories = categories

    def get_id(self):
        return (self.business_id, )

    def to_data(self):
        data = self.__dict__.copy()
        data['sentences'] = [v.to_data() for v in data['sentences']]
        return data

    @classmethod
    def from_data(cls, data):
        data['sentences'] = [Sentence.from_data(v) for v in data['sentences']]
        return cls(**data)
