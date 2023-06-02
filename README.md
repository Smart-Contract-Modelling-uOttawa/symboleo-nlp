# Symboleo NLP

## Description

This project explores techniques for formalizing natural language (NL) customizations to a contract template. A templating approach to contract specification gives flexibility to create a variety of usable contracts without having to start from scratch.

Suppose that we start with a NL contract template T, as well as a Symboleo specification of that template S(T). 

We define a limited set of NL customizations that can be made to a contract template. If a user creates an allowable customization C, then our goal is to formalize that into a Symboleo specification S(C).

Traditional contract templates typically allow a user to customize simple and single-entity blanks (dates, addresses, names, etc.). Such an approach is trivial to formalize, provided we start with a contract template. We are interested in pushing the boundaries of what types of parameters can be automatically formalized. The long view is to have a new NL contract that can be reliably formalized to a specification language (such as Symboleo). This is a very complex problem, so we are making small, but concrete steps towards that goal.  

## Example

** TODO: Add concrete examples

## Requirements

- selection
- mapping

## Controlled Natural language
... description - how we obtained it, etc. 
... grammar and operations

## Running the Project

### Basic Information
The code is written in Python, and makes use of popular NLP functionality, such as [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/). 

Other tools... MLConjug, spacy info, benepar, ...

Other ones explored, but not used 

### Env
- Create a virtual env: python -m venv symboleo-env
- Activate: source symboleo-env/Scripts/activate
- upgrade pip: pip install --upgrade pip
- install requirements: pip install -r requirements.txt
- Ensure that notebooks are using the env as well

in the pyenv.cfg in the venv folder:
- include-system-site-packages = true
- required for protobuf...

next error: Couldn't build proto file into descriptor pool: duplicate file name (sentencepiece_model.proto)


### Inputs and Outputs

S, S(T), ... Manual processes required

In order to function, the application requires the following:
- A NL contract template, with parameters that meet our constraints: T
- A Symboleo specification of the NL contract: S(T)

The applications proceeds as follows:
- The user selects a parameter from the template to customize
- A grammar graph is generated from the parameter details and the contract template. This graph represents all of the valid input the user can enter
- The user enters input by traversing the graph, starting at the root. The result is an ordered list of grammar nodes from the graph
- This node list will correspond to on the allowed NL patterns (a frame). The NL text represented in the frame will have a corresponding Symboleo specification
- The Symboleo contract S(C) is generated accordingly



### Running the Application

Currently a console app. Run using the notebook

### Web Application

...


### Developing

Currently, the code be interactively run and debugged using a Jupyter notebook.


## Testing and Evaluation

Tests to show and explain:
- isolated
- full test
- unit tests
- nlp tests
- show how to run individual files as well

The project is intended to be test-driven. The goal is to define a set of valid test cases for converting NL customizations to Symboleo specifications, and explore how we can get these tests to pass. 
The tests are written with the unittest module and can be run as follows: `python -m unittest tests/file_to_test.py`

To run the full-stack test suites: `python -m unittest tests/test_suites/full_test_suite.py`. These are not part of regular test coverage

To run all unit tests: `python -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app -m unittest discover -s 'tests/unit_tests' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 

## Limitations and Future Work

What it cannot do
- examples of text it cant handle
- event specification
- etc.

Capture some of it as future work


