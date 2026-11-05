# Lab 2 — Build Your First Reusable Python Module

## Business Scenario
Your cleaning logic from Lab 1 is now needed by several future pipelines.

The Data Engineering team does not want the same code copied into every script.

## Requirement
Create:

`portops_utils.py`

It should contain reusable functionality for:
- cleaning ContainerNumber
- cleaning TruckNumber
- converting kilograms to tonnes
- classifying weight
- validating GateDirection

Then create:

`gate_processing.py`

Use functions from `portops_utils.py` inside `gate_processing.py`.

## Test Cases
Process at least five records including:
- a clean record
- a ContainerNumber containing spaces
- a lowercase GateDirection
- a missing TruckNumber
- a heavy container

## Important
Do not copy the function definitions into `gate_processing.py`.

The lab is specifically testing reusable code and imports.


## Engineering Structure Expectation
Where appropriate:
- move repeated logic into functions;
- give functions clear names based on what they do;
- create your own `.py` module when multiple parts of the solution should reuse the same logic;
- import your own functions rather than copying them between scripts.

Do not force a function or module where a few simple lines are clearer.


## Engineering Review
1. What does `import` mean? Import means we are transferring functions called inside a different module to our present .py file for reusability.
2. What does `from portops_utils import ...` mean? It means from this module, we want a specific function, instead of writing the function over again.
3. Why is reusable code better than copying logic? It helps automate task, and helps reusability easier.
4. What is the difference between a function and a method? A function can be either in-built, or customed, either ways, its generic to any data type, and solves a specific task. A method is specific to a specific data type, it is mostly with a .methodname(), and might carry a parameter. 

## Git Submission
Suggested commit:
`Complete Python Lab 2 - reusable module and imports`
