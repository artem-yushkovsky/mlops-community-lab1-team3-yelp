from hypergol import BaseData


class Review(BaseData):

    def __init__(self, review_id: str, user_id: str, business_id: str, stars: float, useful: int, funny: int, cool: int, text: str, date: str):
        self.review_id = review_id
        self.user_id = user_id
        self.business_id = business_id
        self.stars = stars
        self.useful = useful
        self.funny = funny
        self.cool = cool
        self.text = text
        self.date = date

    def get_id(self):
        return (self.business_id, )
