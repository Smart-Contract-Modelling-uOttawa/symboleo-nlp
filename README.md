# Symboleo NLP

## Description

SymboleoNLP is a tool used to formalize natural language (NL) refinements for a contract template into the Symboleo specification Language, which is designed for the domain of smart contract monitoring. A contract that is fully specified in Symboleo can be used on other tools in the Symboleo ecosystem ([model-checking](https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-Compliance-Checker), [compliance-checking](https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-Model-Checker), [code-generation](https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE)). The contract templates are designed to push the flexibility on what can be refined in a contract. Traditional contract templates use simple fill-in-the-blanks (FITB) to be customized by the user. The contract templates used in this project use broader linguistic patterns, giving a contract author much more flexibility. This work can be seen as a step towards full formalization of NL into a specification language like Symboleo.

### Example
We illustrate with an example. Suppose we have a delivery contract template with the following obligation: The seller must deliver the goods to the buyer \[PARAMETER\]. Let us suppose that we have a Symboleo specification for this simple contract template, which might look as follows: `ob_delivery: O(seller, buyer, true, Happens(evt_deliver_goods)`, where `evt_deliver_goods` refers to the delivery event as defined by Symboleo. This specification captures the fact that the seller has an obligation towards to the buyer to make this event happen.

The `PARAMETER` can be filled with a variety of different complex NL values, such as:
- "before March 30, 2023"
- "within 2 weeks of the buyer completing the payment"
- "If the buyer requests delivery"

The tool will process this input into a predictable Symboleo operation, resulting in a refined Symboleo contract. The above NL refinements may result in the following Symboleo refinements:
- `ob_delivery: O(seller, buyer, true, ShappensBefore(evt_deliver_goods, Date("March 30, 2023"))`
- `ob_delivery: O(seller, buyer, true, WhappensBefore(evt_deliver_goods, Date.add(evt_payment, 2, weeks))`
- `ob_delivery: O(seller, buyer, Happens(evt_delivery_request), Happens(evt_deliver_goods))`

### General Process

In general, we will start with a contract template `T` and its corresponding Symboleo specification `S(T)`. The contract author will enter any desired refinements in NL, resulting in a refined NL contract `C`. The role of the tool is to use the inputs `T`,`S(T)`, and `C` to generate the Symboleo that corresponds to the refined NL contract, which we call `S(C)`.

In order to function, the application requires the following:
- A NL contract template, with parameters that meet our constraints `T`. Converting an arbitrary contract to this format is a manual process.
- A Symboleo specification of this NL contract `S(T)`. 

The project includes a variety of contracts pre-formatted for use on the tool. The refinements made by the user are in a _controlled_ Natural Language, which is a subset of NL (English) words and grammar, specialized for the contract domain. This CNL includes various temporal and conditional refinements, as well as a way to specify basic events. 

The tool therefore has two core requirements:
- Enforce that the user's input adheres to the valid CNL.
- Ensure that the CNL refinement that is entered maps to the correct Symboleo refinement.


## Controlled Natural language

The CNL used in this tool is a result of careful research on NL refinements that occur in real contracts and which have mappings to Symboleo operations. It consists of an EBNF grammar and set of mappings between patterns in that grammar and Symboleo operations.


## Running the Project

### Basic Information
The tool is written in Python, and makes use of various NLP libraries, such as:
- [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/): Used for procssing raw NL using a standard NLP pipeline, such as tokenization, POS-tagging, entity recognition.
- [MLConjug](https://pypi.org/project/mlconjug3/): Used for conjugating verbs into various formats.
- [Benepar](https://pypi.org/project/benepar/): Berkeley Neural Parser; Used for constituency parsing.

Other libaries have been explored and may potentially have use in this tool in the future:
- [WordNet](https://www.nltk.org/howto/wordnet.html)
- [Framenet](https://www.nltk.org/howto/framenet.html)
- [Coreferee](https://pypi.org/project/coreferee/)


### Env
Before running the project, set up a virtual environment and install the required packages.
- Create a virtual env: `python -m venv sym-env`
- Activate the environment: `source sym-env/Scripts/activate`
- upgrade pip: `pip install --upgrade pip`. This may require administrative permissions.
- install requirements: `pip install -r requirements.txt`
- Ensure that any relevant notebooks are configured to use the target environment as well

### Running the Application


### NLP Modules

The tool's functionality relies on SpaCy's NLP pipeline for some of the internal processing steps. The `nlp` object must be injected as a dependency into the application. Since this dependency is time-consuming to install, we can generate it in advance, and store it in a pickle file, which is then injected into the application. The construction of this nlp module is done in the `nb_setup.ipynb' notebook. This notebook walks you through the steps of generating the nlp module and then storing it for later use. Since the module is so big (>250MB), it is not pushed up to source control with the rest of the code. 

The functionality that uses the nlp module has been abstracted away into a series of special-purpose classes. In order to facilitate testing, these classes also have "fake" implementations (fakeLemmatizer, fakeNounPhraseExtractor, etc.). The dependency builder for the application takes in an argument that determines whether to use these fake nlp-based classes or the real ones.  

### Console Application

A demo of the tool can currently be run in the nb_console.ipynb notebook. This allows a user to select a pre-loaded contract template, refine the parameters with the CNL, and generate a refined Symboleo specification. This application can be used for limited demonstrations.
  
### Web Application

The Web application provides a much more intuitive user interface to the tool's functionality. A user is able to select from a set of pre-defined sample contracts and enter refinements corresponding to the CNL. Once a refinement is entered, the Symboleo contract is updated with the relevant operations.


## Testing and Evaluation

There are a variety of test sets to demonstrate the reliability of the tool and satisfy the core requirements.
- Unit tests: Basic unit tests for most components used by the tool: `python -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`
- NLP tests: These are specifically designed to test core NLP functionality: `python -m unittest discover -s 'tests/nlp_tests' -p '*_tests.py'`
- Full test suite: These are designed to test the functionality on an entire NL contract `T` and its specification `S(T)`. These tests do not perform specific validation on the generated Symboleo, but the artifacts can be used to manually inspect the tool's performance, and also provide a general benchmark for how the tool performs against realistic contract: `python -m unittest tests/full_tests/full_test_suite.py`
- Isolated test suites: These are designed to test the second requirement of ensuring the CNL input is mapped to the proper Symboleo. These test cases are NL refinements taken from real contracts, where we've taken a single obligation in _isolation_ and modelled the expected results in Symboleo: `python -m unittest tests/full_tests/isolated_test_suite.py`
- Individual tests can be run as well: `python -m unittest tests/file_to_test.py`
- To run _all_ tests: `python -m unittest discover -s 'tests' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 

## Deployment

The web application can be deployed to an environment capable of hosting a Python/Flask application. We have successfully experimented with [pythonanywhere](https://www.pythonanywhere.com/). These are the steps to deploy:
- Set up an account on pythonanywhere
- Configure your account to connect to GitHub via ssh. [This video](https://www.youtube.com/watch?v=4sTZN15J33A&ab_channel=KevinTech) provides a detailed overview
- Using a console in the pythonanywhere web application, clone the repo using ssh. This will load the files from GitHub into the pythonanywhere environment
- Create a new web application in pythonanywhere. Ensure it is a Flask application using Python 3.9.
- Configure the web application to use the /web.py file as the entry point to the application.
- Going back to the web console, install the requirements: `pip3.9 install -r requirements.txt'. The pip version must align with the Python version selected in the web app creation, otherwise you may get import errors.
- Re-deploy the web app from pythonanywhere

A challenge facing deployment is the proper integration of Spacy's nlp module. The free tier for pythonanywhere has limited storage, so in some cases it cannot handle the large file. As a workaround, the "fake" nlp classes can be used for demonstration purposes. 


## Todos

- Update to use a production server
- Add a config file
- Minor grammar improvements (e.g. relevant capitalization and punctuation)
- Further CNL constraints on specific parameters



