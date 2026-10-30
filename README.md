# Second CI/CD Pipeline (Programs 31–40)

This repository contains Python programming assignments (Programs 31 through 40) structured with source code in codes_4 and test suites in test_code_4, validated via an automated GitHub Actions CI/CD pipeline.

## Repository Structure

Second_CI_Pipeline/
|-- __init__.py
|-- requirements.txt
|-- .github/workflows/ci.yml
|-- codes_4/ (Programs 31 to 40 .py files)
|-- test_code_4/ (Corresponding test files using importlib)

## Workflow Guidelines

1. Feature Branches: Every program has been developed on its own isolated feature branch.
2. Dynamic Imports: Because script filenames start with digits, test files use Python's importlib.util module to dynamically load modules from the codes_4 directory.
3. Automated CI: Pull Requests targeting main automatically run syntax checking via compileall and execute test suites against the test_code_4 directory using pytest.
