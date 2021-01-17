from hypergol import BaseData


class Hour(BaseData):

    def __init__(self, Monday: str, Tuesday: str, Wednesday: str, Thursday: str, Friday: str, Saturday: str, Sunday: str):
        self.Monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday
        self.Saturday = Saturday
        self.Sunday = Sunday
