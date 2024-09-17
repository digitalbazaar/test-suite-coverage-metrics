# Test-Suites Coverage Metrics

## Abstract

This repository displays some metrics around the coverage of W3C test-suites in relation to the Specifications they aim to demonstrate conformance for.

## Disclaimer

The outputs are not meant to be a final assessment of test coverage. Their goal is to provide guidance when asserting if test-suites are missing test cases.

## Methodology

When creating a test-suite, developers will transform normative statements from a specification into test cases. All test-suites are written in javascript with the mocha chai test framework. A custom Digital Bazaar reporter then renders the results and publishes conformity reports.

To assess the test coverage, the scripts included in this repo will take a test-suite report url and an array of respec url. Each test cases from the report will be added to an array, and each normative statements from every linked specification will be added in second array.

These arrays are then compared with the difflib built-in python library, setting a match treshold (currently set at a 0.75 value). When a match is found, the statement is removed from each array.

The following are cases that might create false positive matches:
- Very similar spec statements.
- Modified spec statements to add context.
- Duplicate tests of the same statement (issuer and verifier)
- Different order of appearance
- Test-suites covering more than 1 specification

## Outputs

For each test suites, the output will contain the following:
- Key metrics
- Matched statement pairs
- All statement arrays from the test-suite report and related specifications
- Unmatched statement arrays  from the test-suite report and related specifications

## Current coverage
- [vc-data-model-2.0-test-suite](./outputs/vc-data-model-2.0-test-suite.md)
- [vc-bitstring-status-list-test-suite](./outputs/vc-bitstring-status-list-test-suite.md)
- [vc-di-bbs-test-suite](./outputs/vc-di-bbs-test-suite.md)
- [vc-di-eddsa-test-suite](./outputs/vc-di-eddsa-test-suite.md)
- [vc-data-model-2.0-test-suite](./outputs/vc-di-bbs-test-suite.md)

