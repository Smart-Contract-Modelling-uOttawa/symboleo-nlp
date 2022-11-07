# Symboleo Natural Language Project

## Overview
This project explores techniques for formalizing natural language (NL) updates to a contract template. Suppose that we start with a NL contract template T, as well as a Symboleo specification of that template S(T). 
Contract templates are useful because they can be customized in a variety of ways to create usable contracts without having to start a contract from scratch.
We define a limited set of NL customizations that can be made to a contract template. If a user creates an allowable customization C, then our goal is to formalize that into a Symboleo specification S(C).

Examples of customization may include adding conjunctions or disjunctions onto existing components of the contract template (i.e. the trigger, antecedent, consequent). 

** TODO: Define the set of allowable customizations (this is an RQ)

## Example

** TODO: Add concrete examples

## Tools and Techniques
The code is written in Python, and makes use of popular NLP functionality, such as [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/). 

** TODO: Discuss dependency parsing

** TODO: Discuss constituency parsing (benepar)

** TODO: Discuss ML (if applicable)

## Running

Currently, the code be interactively run and debugged using a Jupyter notebook.

The project is intended to be test-driven. The goal is to define a set of valid test cases for converting NL customizations to Symboleo specifications, and explore how we can get these tests to pass. 
The tests are written with the unittest module and can be run as follows: `python -m unittest tests/file_to_test.py`

To run all unit tests: `python -m unittest discover -s 'tests/' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app/src -m unittest discover -s 'tests/' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 

## Next Steps

Before starting to explore NLP extraction techniques, need to do the following:  
- Complete the Symboleo class specification in Python (i.e. add more atoms, situation types, etc.)
- Add 1-2 more completed templates (e.g. rent2own, sales, independent contractor, rental)
- Start building a list of customizations and creating corresponding tests


source symboleo-env/Scripts/activate