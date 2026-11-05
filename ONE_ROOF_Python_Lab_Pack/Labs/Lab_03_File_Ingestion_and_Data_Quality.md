# Lab 3 — File Ingestion and Data Quality

## Business Scenario
Gate Operations now sends transactions as a CSV file.

Use:
`Data/PortOps_Gate_Transactions_Dirty.csv`

You are building the first stage of an ingestion process.

## Business Requirements
Your Python program must:
- read the file;
- determine how many records were received;
- identify records with missing TransactionID;
- identify records with missing TruckNumber;
- identify invalid GateDirection values;
- identify GrossWeightKg values that cannot be treated as numbers;
- preserve invalid records rather than silently discarding them.

Produce:
- `gate_valid.csv`
- `gate_rejected.csv`

Rejected records must contain:
- `RejectReason`

## Execution Summary
Display:
- RowsRead
- RowsAccepted
- RowsRejected
- MissingTransactionID
- MissingTruckNumber
- InvalidGateDirection
- InvalidWeight

## Failure Requirement
Handle a missing source file without an uncontrolled crash.

## Logging Requirement
Create meaningful messages for:
- pipeline start;
- source file received;
- rows processed;
- rejected records;
- pipeline success/failure.


## Engineering Structure Expectation
Where appropriate:
- move repeated logic into functions;
- give functions clear names based on what they do;
- create your own `.py` module when multiple parts of the solution should reuse the same logic;
- import your own functions rather than copying them between scripts.

Do not force a function or module where a few simple lines are clearer.


## Engineering Review
1. Why should rejected records be preserved?
2. Why is `print()` alone insufficient for a production pipeline?
3. What should happen when the expected input file is missing?
4. Which validation rules deserve their own functions?

## Git Submission
Suggested commit:
`Complete Python Lab 3 - file ingestion and validation`
