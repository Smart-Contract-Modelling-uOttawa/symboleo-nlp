# Symboleo NLP

## Description

SymboleoNLP is a tool used to formalize natural language (NL) refinements for a contract template into the Symboleo specification Language, which is designed for the domain of smart contract monitoring. A contract that is fully specified in Symboleo can be used on other tools in the Symboleo ecosystem (model-checking, compliance-checking, code-generation). (*** add links here) The contract templates are designed to push the flexibility on what can be refined in a contract. Traditional contract templates use simple fill-in-the-blanks for the user. The contract templates used in this project use broader linguistic patterns, giving a contract author much more flexibility. This work can be seen as a step towards full formalization of NL into a specification language like Symboleo.

### Example
We illustrate with an example. Suppose we have a delivery contract template with the following obligation: The seller must deliver the goods to the buyer \[PARAMETER\]. Let us suppose that we have a Symboleo specification for this simple contract template, which might look as follows: `ob_delivery: O(seller, buyer, T, Happens(evt_deliver_goods)`, where `evt_delivery` corresponds to a specification of the delivery event. This specification captures the fact that the seller has an obligation towards to the buyer to make this event happen.

The `PARAMETER` can be filled with a variety of different complex NL values, such as:
- "before March 30, 2023"
- "within 2 weeks of the buyer completing the payment"
- "If the buyer requests delivery"

The tool will process this input into a predictable Symboleo operation, resulting in a refined Symboleo contract. The above NL refinements may result in the following Symboleo refinements:
- `ob_delivery: O(seller, buyer, T, SHappensBefore(evt_deliver_goods, Date("March 30, 2023"))`
- `ob_delivery: O(seller, buyer, T, WHappensBefore(evt_deliver_goods, Date.add(evt_payment, 2, weeks))`
- `ob_delivery: O(seller, buyer, Happens(evt_delivery_request), Happens(evt_deliver_goods)`

### General Process

In general, we will start with a contract template `T` and its corresponding Symboleo specification `S(T)`. The contract author will enter any desired refinements in NL, resulting in a refined NL contract `C`. The role of the tool is to use the inputs `T`,`S(T)`, and `C` to generate the Symboleo that corresponds to the refined NL contract, which we call `S(C)`.

In order to function, the application requires the following:
- A NL contract template, with parameters that meet our constraints `T`. Converting an arbitrary contract to this format is a manual process
- A Symboleo specification of this NL contract `S(T)`. 

The project includes a variety of contracts pre-formatted for use on the tool. The refinements made by the user are in a _controlled_ Natural Language, which is a subset of NL (English) words and grammar, specialized for the contract domain. This CNL includes various temporal and conditional refinements, as well as a way to specify basic events. 

The tool therefore has two core requirements:
- Enforce that the user's input adheres to the valid CNL
- Ensure that the CNL refinement that is entered maps to the correct Symboleo refinement


## Controlled Natural language

The CNL used in this tool is a result of careful research on NL refinements that occur in real contracts and which have mappings to Symboleo operations. It consists of an EBNF grammar and set of mappings between patterns in that grammar and Symboleo operations.

*** present the grammar

*** present the operation table

## Running the Project

### Basic Information
The tool is written in Python, and makes use of various NLP libraries, such as:
- [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/): Used for procssing raw NL using a standard NLP pipeline, such as tokenization, POS-tagging, entity recognition  
- MLConjug
- Benepar

Other libaries have been explored and may potentially have use in this tool in the future:
- WordNet...
- Framenet...
- Coreferee...


### Env
Before running the project, set up a virtual environment and install the required packages.
- Create a virtual env: python -m venv symboleo-env
- Activate: source sym-env/Scripts/activate
- upgrade pip: pip install --upgrade pip
- install requirements: pip install -r requirements.txt
- Ensure that notebooks are using the env as well

<!-- in the pyenv.cfg in the venv folder:
- include-system-site-packages = true
- required for protobuf... -->
<!-- next error: Couldn't build proto file into descriptor pool: duplicate file name (sentencepiece_model.proto)
 -->


### Running the Application

A demo of the tool can currently be run in the nb_demo.ipynb notebook. This allows a user to select a pre-loaded contract template, refine the parameters with the CNL, and generate a refined Symboleo specification.

### Web Application

...


## Testing and Evaluation

There are a variety of test sets to demonstrate the reliability of the tool and satisfy the core requirements.
- Unit tests: Basic unit tests for most components used by the tool: `python -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`
- NLP tests: These are specifically designed to test core NLP functionality: `python -m unittest discover -s 'tests/nlp_tests' -p '*_tests.py'`
- Full test suite: These are designed to test the functionality on an entire NL contract `T` and its specification `S(T)`. These tests do not perform specific validation on the generated Symboleo, but the artifacts can be used to manually inspect the tool's performance, and also provide a general benchmark for how the tool performs against realistic contract: `python -m unittest tests/test_suites/full_test_suite.py`
- Isolated test suites: These are designed to test the second requirement of ensuring the CNL input is mapped to the proper Symboleo. These test cases are NL refinements taken from real contracts, where we've taken a single obligation in _isolation_ and modelled the expected results in Symboleo: `python -m unittest tests/test_suites/isolated_test_suite.py`
- Individual tests can be run as well: `python -m unittest tests/file_to_test.py`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 

## Limitations and Future Work

What it cannot do
- examples of text it cant handle...
- event specification...
- ...

Capture some of this as future work


