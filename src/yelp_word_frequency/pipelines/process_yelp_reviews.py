import os
import fire
from hypergol import HypergolProject
from hypergol.hypergol_project import RepoManager
from hypergol import Pipeline
from tasks.create_businesses import CreateBusinesses
from tasks.create_reviews import CreateReviews
from tasks.create_review_documents import CreateReviewDocuments
from data_models.business import Business
from data_models.review import Review
from data_models.review_document import ReviewDocument

# export BASE_DIRECTORY='/home/<user_name>'
BASE_DIRECTORY = os.environ['BASE_DIRECTORY']

def process_yelp_reviews(threads=1, force=False):
    project = HypergolProject(
        dataDirectory=f'{BASE_DIRECTORY}/reviews', 
        repoManager=RepoManager(
            repoDirectory=f'{BASE_DIRECTORY}/Yelp_Dataset', 
            raiseIfDirty=not force
        ),
        force=force
    )

    businesses = project.datasetFactory.get(dataType=Business, name='businesses')
    reviews = project.datasetFactory.get(dataType=Review, name='reviews')
    reviewDocuments = project.datasetFactory.get(dataType=ReviewDocument, name='review_documents')

    createBusinesses = CreateBusinesses(
        yelpBusinessJsonPath=f'{BASE_DIRECTORY}/reviews/yelp_academic_dataset_business.json',
        splits=20,
        outputDataset=businesses,
    )
    createReviews = CreateReviews(
        yelpReviewsJsonPath=f'{BASE_DIRECTORY}/reviews/yelp_academic_dataset_business.json', 
        splits=20,
        outputDataset=reviews,
    )
    createReviewDocuments = CreateReviewDocuments(
        inputDatasets=[reviews],
        loadedInputDatasets=[businesses],
        outputDataset=reviewDocumentss,
    )

    pipeline = Pipeline(
        tasks=[
            createBusinesses,
            createReviews,
            createReviewDocuments,
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(process_yelp_reviews)
