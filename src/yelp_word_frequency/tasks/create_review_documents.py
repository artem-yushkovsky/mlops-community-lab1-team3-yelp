import spacy
from hypergol import Task
from data_models.review import Review
from data_models.review_document import ReviewDocument
from data_models.sentence import Sentence
from data_models.token import Token


class CreateReviewDocuments(Task):

    def __init__(self, spacyModelName, *args, **kwargs):
        super(CreateReviewDocuments, self).__init__(*args, **kwargs)
        self.spacyModelName = spacyModelName
        self.categories = None

    def init(self):
        self.spacyModel = spacy.load(self.spacyModelName)
        self.categories = {business.business_id: business.categories for business in self.loadedData[0]}

    def run(self, review, businesses):
        reviewDocument = Article(
            review_id=review.review_id,
            user_id=review.user_id,
            business_id=review.business_id,
            stars=review.stars,
            useful=review.useful,
            funny=review.funny,
            cool=review.cool,
            text=review.text,
            date=review.date,
            sentences=[],
            categories=self.categories[review.business_id]
        )
        for k, sentence in enumerate(self.spacyModel(review.text).sents):
            tokenOffset = sentence[0].i
            tokenCharOffset = sentence[0].idx
            reviewDocument.sentences.append(Sentence(
                startChar=sentence[0].idx,
                endChar=sentence[-1].idx+len(str(sentence[-1])),
                articleId=article.articleId,
                sentenceId=k,
                tokens=[Token(
                    i=token.i-tokenOffset,
                    startChar=token.idx-tokenCharOffset,
                    endChar=token.idx+len(str(token))-tokenCharOffset,
                    depType=token.dep_,
                    depHead=token.head.i-tokenOffset,
                    depLeftEdge=token.left_edge.i-tokenOffset,
                    depRightEdge=token.right_edge.i-tokenOffset,
                    posType=token.pos_,
                    posFineType=token.tag_,
                    lemma=token.lemma_,
                    text=token.text
                ) for token in sentence]
            ))
        self.output.append(reviewDocument)
