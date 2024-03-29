# NL/Symboleo Specifications

## Full Contracts

This directory contains fully specified Symboleo specifications of a variety of NL contracts.

The following contracts are used:
- A meat sale contract between a buyer and seller: [Link](https://github.com/reganmeloche/symboleo-nlp/tree/main/app/templates/meat_sale/t_raw)
- A rental contract between a renter and owner: [Link](https://github.com/reganmeloche/symboleo-nlp/tree/main/app/templates/rental/t_raw)
- A property management contract between an owner and manager: [Link](https://github.com/reganmeloche/symboleo-nlp/tree/main/app/templates/prop/t_raw)
- A biomass supply contract between a buyer and seller: [Link](https://github.com/reganmeloche/symboleo-nlp/tree/main/app/templates/biomass/t_raw)
- An independent contractor contract between a client and a contractor: [Link](https://github.com/reganmeloche/symboleo-nlp/tree/main/app/templates/indep/t_raw)

These contracts can be reviewed by clicking on the link and inspecting the NL strings corresponding to the contract (nl_template.py file) as well as the corresponding Symboleo (xxxxx_raw.txt file) 

For each of these contracts, there is a corresponding broadened version of the NL and Symboleo. We also have an accompanying suite of CNL refinements for each that attempts to recreate the original contract (NL and Symboleo). These tests do not yet specifically compare the actual and expected results, but the results are output to a set of files for manual inspection. More specific testing is done on the isolated test cases (below). These "full" tests are intended to show how the tool works holistically on a variety of contracts, and can motivate a road map for future work on the tool.


## Isolated Test Suite

We have a separate set of tests that are based on real contracts found in the CUAD dataset. For these tests, we've only extracted a single NL norm from a given contract. From this single norm, we create an _assumed_ Symboleo specification, which includes assumed domain objects and declarations that are needed to specify the norm in Symboleo. 

For each norm, we have an expected refined Symboleo contract which is precisely tested. All of the relevant files are found in [this directory](https://github.com/reganmeloche/symboleo-nlp/tree/main/tests/test_suites/isolated_results). For each isolated norm, we have the following files:
- xxxx_nl.py: Shows the results generated by the tool (A) and the expected values (E), which are derived from (but not identical to) the real NL contract. These must be identical or the test will fail.
- xxxx_sym_init.txt: The initial Symboleo template T before the refinement is applied
- xxxx_sym_actual.txt: The Symboleo that is generated when the tool processes the NL refinement
- xxxx_sym_expected.txt: The _expected_ Symboleo for each refinement. The sym_actual and sym_expected files are tested for equality
