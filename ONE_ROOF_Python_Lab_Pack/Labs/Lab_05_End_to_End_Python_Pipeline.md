# Lab 5 — End-to-End Python Data Engineering Pipeline

## Business Scenario
Every morning Gate Operations places a file in an inbound folder.

Management wants a repeatable process that prepares trusted data for downstream reporting.

Use:
- `Data/PortOps_Gate_Transactions_Dirty.csv`
- `Data/PortOps_Lane_Lookup.csv`

## Required Flow
RAW FILE
→ READ
→ PROFILE
→ VALIDATE
→ CLEAN
→ REJECT INVALID
→ ENRICH
→ WRITE TRUSTED OUTPUT
→ LOG RESULT

## Business Requirements
Your pipeline must:
- detect/read the incoming source file;
- profile the dataset;
- validate required columns;
- clean ContainerNumber;
- clean TruckNumber;
- standardize GateDirection;
- convert dates and numeric columns;
- detect duplicate TransactionID;
- reject invalid records;
- enrich with Lane information;
- calculate GrossWeightTons;
- classify WeightClass.

## Expected Outputs
Create:
- `/clean/gate_transactions_clean.csv`
- `/reject/gate_transactions_rejected.csv`
- `/logs/pipeline.log`

## Run Summary
Every execution must report:
- SourceFile
- RowsRead
- RowsValid
- RowsRejected
- DuplicateTransactions
- MissingTruckNumbers
- StartTime
- EndTime
- Status

## Reusability Requirement
Do not place everything inside one giant script.

Use functions where they make individual responsibilities clearer.

Create at least one reusable module for logic that should not live directly inside the main orchestration script.

A possible structure is:

```text
project/
├── main.py
├── portops_utils.py
├── inbound/
├── clean/
├── reject/
└── logs/
```

You do not have to use these exact names.


## Engineering Structure Expectation
Where appropriate:
- move repeated logic into functions;
- give functions clear names based on what they do;
- create your own `.py` module when multiple parts of the solution should reuse the same logic;
- import your own functions rather than copying them between scripts.

Do not force a function or module where a few simple lines are clearer.


## Rerun Questions
Run the pipeline twice with the same source data.

Answer:
1. What would happen if the clean output were loaded into a database?
2. How would you prevent the same TransactionID from being loaded twice?
3. If a previously loaded TransactionID arrives with corrected data, what should the pipeline do?
4. Which parts of your pipeline belong in `main.py`, and which belong in a reusable module?

## Git Submission
Suggested commit:
`Complete Python Lab 5 - end to end PortOps pipeline`
