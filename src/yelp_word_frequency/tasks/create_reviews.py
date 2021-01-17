from hypergol import Job
from hypergol import Task
from data_models.review import Review


class CreateReviews(Task):

    def __init__(self, yelpReviewsJsonPath, splits, *args, **kwargs):
        super(CreateReviews, self).__init__(*args, **kwargs)
        self.yelpReviewsJsonPath = yelpReviewsJsonPath
        self.splits = splits

    def get_jobs(self):
        return [Job(
            id_=split, 
            total=self.splits,
            parameters={'split': split}
        ) for split in range(self.splits)]

    def source_iterator(self, parameters):
        with open(self.yelpReviewsJsonPath) as reviewFile:
            for line in islice(reviewFile, parameters['split'], None, self.splits):
                yield (json.loads(line), )

    def run(self, data):
        self.output.append(Review(
            review_id=data['review_id'],
            user_id=data['user_id'],
            business_id=data['business_id'],
            stars=data['stars'],
            useful=data['useful'],
            funny=data['funny'],
            cool=data['cool'],
            text=data['text'],
            date=data['date']
        ))
