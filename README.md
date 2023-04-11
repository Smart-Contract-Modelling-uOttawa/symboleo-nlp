# Symboleo Natural Language Project

## Overview
This project explores techniques for formalizing natural language (NL) customizations to a contract template. A templating approach to contract specification gives flexibility to create a variety of usable contracts without having to start from scratch.

Suppose that we start with a NL contract template T, as well as a Symboleo specification of that template S(T). 

We define a limited set of NL customizations that can be made to a contract template. If a user creates an allowable customization C, then our goal is to formalize that into a Symboleo specification S(C).

Traditional contract templates typically allow a user to customize simple and single-entity blanks (dates, addresses, names, etc.). Such an approach is trivial to formalize, provided we start with a contract template. We are interested in pushing the boundaries of what types of parameters can be automatically formalized. The long view is to have a new NL contract that can be reliably formalized to a specification language (such as Symboleo). This is a very complex problem, so we are making small, but concrete steps towards that goal.  

## Example

** TODO: Add concrete examples

## Available customizations

We focus on customizations that are optional (**explain this more)

We currently allow for the following NL patterns:
** Provide patterns with examples

### Predicate Refinement
The following patterns result in a refinement of a Symboleo "Happens" predicate:
- Before/"prior to" DATE/EVENT
- Within TIMESPAN of EVENT
- After DATE/EVENT
- ...HappensWithin...

### Adding a Trigger
The following patterns result in an added trigger to a selected norm.
- If/Upon/"in case"/"in the event"/... EVENT

### Adding a Norm
The following two patterns result in the addition of a power related to an existing norm. Specifically this new norm has the power to suspend the norm that it is related to
- Until EVENT/DATE
- Unless EVENT

### Adding a Domain Property
The following patterns result in the addition of new domain model properties. This is a very open-ended category, as there will be many ways to linguistically represent this type of operation. 
- Using INSTRUMENT
- By METHOD
- With PROPERTY VALUE
- ...

Each of these patterns has a reliable mapping to a Symboleo refinement. By controlling the available customizations by these NL patterns, we ensure that we always generate a valid Symboleo contract.

The controlled NL patterns can be expanded to allow for more expressiveness and flexibility on what can be entered. More expressiveness is inherently desirable, but in general, adding expressive and flexible patterns can be harder to process, leading to less reliable mappings to Symboleo.

## Tools and Techniques
The code is written in Python, and makes use of popular NLP functionality, such as [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/). 

** TODO: Discuss dependency parsing

** TODO: Discuss constituency parsing (benepar)

** TODO: Discuss ML (if applicable)

## Running

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

### Developing

Currently, the code be interactively run and debugged using a Jupyter notebook.

The project is intended to be test-driven. The goal is to define a set of valid test cases for converting NL customizations to Symboleo specifications, and explore how we can get these tests to pass. 
The tests are written with the unittest module and can be run as follows: `python -m unittest tests/file_to_test.py`

To run the full-stack test suites: `python -m unittest tests/run_test_suites.py`. These are not part of regular test coverage

To run all unit tests: `python -m unittest discover -s 'tests/' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app -m unittest discover -s 'tests/' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 

## Process

In order to function, the application requires the following:
- A NL contract template, with parameters that meet our constraints: T
- A Symboleo specification of the NL contract: S(T)

The applications proceeds as follows:
- The user selects a parameter from the template to customize
- A grammar graph is generated from the parameter details and the contract template. This graph represents all of the valid input the user can enter
- The user enters input by traversing the graph, starting at the root. The result is an ordered list of grammar nodes from the graph
- This node list will correspond to on the allowed NL patterns (a frame). The NL text represented in the frame will have a corresponding Symboleo specification
- The Symboleo contract S(C) is generated accordingly


## Next Steps

### Current Status

The application currently has the following features:
- Have a grammar generator, selector, and frame mapping infratructure set up 
- Can run basic demos - they are full-stack - goes all the way through the whole process
- Old code is cleaned out and folder is appropriately structured
- We have a growing test suite and good coverage
- We have a list of frames that need to be added


### TODOS
Main priorities:
- Get a basic sample of each operation
- decide on the HappensWithin refinement
- Look more closely at EVENT specification
- Bring in WordNet or other tools for DM props

### Longer term
Longer term goals:

- reverse verification: e.g. Take NL sentence as input and verify it corresponds to nodes in the tree - output the possibilities

