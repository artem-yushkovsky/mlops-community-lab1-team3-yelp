import json
from itertools import islice
from hypergol import Job
from hypergol import Task
from data_models.business import Business


class CreateBusinesses(Task):

    def __init__(self, yelpBusinessJsonPath, splits, *args, **kwargs):
        super(CreateBusinesses, self).__init__(*args, **kwargs)
        self.yelpBusinessJsonPath = yelpBusinessJsonPath
        self.splits = splits

    def get_jobs(self):
        return [Job(
            id_=split, 
            total=self.splits,
            parameters={'split': split}
        ) for split in range(self.splits)]

    def source_iterator(self, parameters):
        with open(self.yelpBusinessJsonPath) as businessFile:
            for line in islice(businessFile, parameters['split'], None, self.splits):
                yield (json.loads(line), )

    def run(self, data):
        self.output.append(Business(
            business_id=data['business_id'],
            name=data['name'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            postal_code=data['postal_code'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            stars=data['stars'],
            review_count=data['review_count'],
            is_open=data['is_open'],
            attributes=[],
            categories=[category.strip() for category in data['categories'].split(',')],
            hours=[]
        ))
