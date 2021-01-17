# YelpWordFrequency


python -m hypergol.cli.create_project YelpWordFrequency

python -m hypergol.cli.create_data_model Attribute BusinessAcceptsCreditCards:str BikeParking:str GoodForKids:str BusinessParking:str ByAppointmentOnly:str RestaurantsPriceRange2:str DogsAllowed:str WiFi:str RestaurantsAttire:str RestaurantsTakeOut:str NoiseLevel:str RestaurantsReservations:str RestaurantsGoodForGroups:str HasTV:str Alcohol:str RestaurantsDelivery:str OutdoorSeating:str Caters:str WheelchairAccessible:str AcceptsInsurance:str RestaurantsTableService:str Ambience:str GoodForMeal:str HappyHour:str BusinessAcceptsBitcoin:str BYOB:str Corkage:str GoodForDancing:str CoatCheck:str BestNights:str Music:str Smoking:str DietaryRestrictions:str DriveThru:str HairSpecializesIn:str BYOBCorkage:str AgesAllowed:str RestaurantsCounterService:str Open24Hours:str --force

python -m hypergol.cli.create_data_model Hour Monday:str Tuesday:str Wednesday:str Thursday:str Friday:str Saturday:str Sunday:str --force

python -m hypergol.cli.create_data_model Business business_id:str name:str address:str city:str state:str postal_code:str latitude:float longitude:float stars:float review_count:int is_open:int "attributes:List[Attribute]" "categories:List[str]" "hours:List[Hour]" --force

python3 -m hypergol.cli.create_data_model Review review_id:str user_id:str business_id:str:id stars:float useful:int funny:int cool:int text:str date:str --force

python -m hypergol.cli.create_data_model Token i:int startChar:int endChar:int depType:str depHead:int depLeftEdge:int depRightEdge:int posType:str posFineType:str lemma:str text:str
python -m hypergol.cli.create_data_model Sentence startChar:int endChar:int articleId:int:id sentenceId:int:id "tokens:List[Token]"
python -m hypergol.cli.create_data_model ReviewDocument review_id:str user_id:str business_id:str:id stars:float useful:int funny:int cool:int text:str date:str "sentences:List[Sentence]"

python3 -m hypergol.cli.create_task CreateBusinesses Business --source
python3 -m hypergol.cli.create_task CreateReviews Review --source
python3 -m hypergol.cli.create_task CreateReviewDocuments Review ReviewDocument Sentence Token

python3 -m hypergol.cli.create_pipeline ProcessYelpReviews CreateBusinesses CreateReviews CreateReviewDocuments Business Review ReviewDocument




This project was generated with the Hypergol framework

Please see documentation for instructions: [https://hypergol.readthedocs.io/en/latest/](https://hypergol.readthedocs.io/en/latest/)

### Initialise git

Hypergol is heavily integrated with git, all projects must be in a git repository to ensure code and data lineage (to record which data was created by which version of the code).

Initialise git with:

```git init .```

Create the first commit (datasets record the last commit when they are created and without this there is nothing to record):

```git commit -m "First Commit!"```

The project now (and any time a file is changed but the change is not committed to the repo) is in a "dirty" stage. If you run a pipeline or train a model, the last commit will be recorded but that commit will not represent the code that is running! Add changes and commit:

```
git add .
git commit -m "All the files!"
```

If there are files that shouldn't be checked in ever to git they should be to the `.gitignore` file before `git add .`

Alternatively individual files can be added to git with `git add <filename>`.

### Make the virtual environment

Having dedicated virtual environment fully described by the projects `requirements.txt` is the recommended practice. Don't forget to `deactivate` the current virtual environment! Files from the environment are included in the projects `.gitignore` file and will ignored by git.

```
deactivate
./make_venv.sh
source .venv/bin/activate
```


### How to list existing Datasets (in Jupyter)

```
from hypergol import HypergolProject
project = HypergolProject(
    projectDirectory='<project_directory>/yelp_word_frequency',
    dataDirectory='<data_directory>'
)
project.list_datasets(pattern='.*', asCode=True);
```

This will list all existing datasets that matches `pattern` as self contained executable code.


### How to start Tensorboard

It is recommended to start it in a screen session (`screen -S tensorboard`) so you can close the terminal window or if you disconnect from a remote Linux machine (reconnect with `screen -x tensorboard`). In the project directory:

```
screen -S tensorboard
source .venv/bin/activate
tensorboard --logdir=<data_directory>/yelp_word_frequency/tensorboard/
```


### How to train your model

After implementing all components and required functions:

```
./train_yelp_word_frequency.sh
```

This will execute the model manager's run() function with the prescribed schedule (training steps, evaluation steps, etc.). Training can be stopped with Ctrl-C, this will won't result in the corruption of the output dataset (datasets must be closed properly to generate their chk file after they are read only). This is possible because the entire training happen in a `try/finally` block.

### How to serve your model

In the generated `models/serve_yelp_word_frequency.py` function specify the directory of the model to be served at:

```
MODEL_DIRECTORY = '<data_directory>/yelp_word_frequency/<branch>/models/<ModelName>/<epoch_number>'
```

then start serving with (port and host can be set in the shell script):

```
./serve_yelp_word_frequency.sh
```


### How to call your model from python with requests

```
import requests
response = json.loads(requests.get('http://0.0.0.0:8000', headers={'accept': 'application/json'}).text)
modelLongName = response['model']
```

This allows to verify if indeed the intended model is served. The generated training script sets training day and the commit hash at that point to be part of the long name and to ensure that the exact conditions of training are available at serving. Long name should be used in logging to identify which model created an output. From v0.0.10 the long name is returned in the header of the response of `/output` endpoint as well in the `x-model-long-name` field.

To get the response of the model to a list of objects, see example below. Replace `ExampleOutput` with the correct output type and load a dataset into `ds`, use `list_datasets` from above to do this.

```
sys.path.insert(0, '<project_directory>/yelp_word_frequency')
import requests
from itertools import islice

from data_models.example_output import ExampleOutput


with ds.open('r') as dsr:
    values = [value.to_data() for value in islice(dsr, 10)]


response = requests.post(
    'http://0.0.0.0:8000/output',
    headers={
        'accept': 'application/json',
        'Content-Type': 'application/json',
    },
    data=json.dumps(values)
)
outputs = [ExampleOutput.from_data(v) for v in json.loads(response.text)]
modelLongName = response.headers['x-model-long-name']
```

It is not recommended to do large scale evaluation through the API as the overhead per object is too high and it is single threaded.
