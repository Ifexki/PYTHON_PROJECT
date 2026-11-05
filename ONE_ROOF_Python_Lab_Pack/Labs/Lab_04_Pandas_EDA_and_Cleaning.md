# Lab 4 — Pandas Data Profiling, EDA and Cleaning

## Business Scenario
Before transforming the Gate Transaction dataset, the Data Engineering team wants you to understand the data first.

Use:
`Data/PortOps_Gate_Transactions_Dirty.csv`

> Do not immediately start cleaning. Profile the data first.

## Part A — EDA / Data Discovery
Produce evidence showing:
- number of rows and columns;
- column names;
- sample rows from the beginning;
- sample rows from the end;
- data types;
- DataFrame information;
- descriptive statistics;
- NULL count by column;
- duplicate row count;
- unique GateDirection values;
- frequency of each GateDirection;
- distinct ContainerNumber count;
- minimum GrossWeightKg;
- maximum GrossWeightKg;
- average GrossWeightKg.

### Pandas EDA method family
You are expected to work with methods/properties such as:
- `head()`
- `tail()`
- `shape`
- `columns`
- `dtypes`
- `info()`
- `describe()`
- `isna()`
- `duplicated()`
- `unique()`
- `nunique()`
- `value_counts()`
- `min()`
- `max()`
- `mean()`

## Part B — Clean the Dataset
Business rules:
- standardize ContainerNumber;
- standardize TruckNumber;
- standardize GateDirection;
- convert TransactionTime to datetime;
- convert GrossWeightKg to numeric;
- identify duplicate TransactionID;
- preserve one valid occurrence where appropriate;
- separate invalid records;
- create GrossWeightTons;
- create WeightClass.

## Part C — Business Analysis
Produce a Gate Direction Summary containing:
- GateDirection
- Transactions
- DistinctContainers
- AverageWeightTons
- MaximumWeightTons

Then answer:
- Which GateDirection has the most transactions?
- How many heavy transactions occurred?
- How many containers have no TruckNumber recorded?

## Validation
Record:
- RowsBefore
- RowsAfter
- DuplicateTransactions
- RejectedRows
- NullTransactionIDs


## Engineering Structure Expectation
Where appropriate:
- move repeated logic into functions;
- give functions clear names based on what they do;
- create your own `.py` module when multiple parts of the solution should reuse the same logic;
- import your own functions rather than copying them between scripts.

Do not force a function or module where a few simple lines are clearer.


## Engineering Review
1. Why is EDA important before writing transformations?
2. Which cleaning rules would you move into reusable functions?
3. If those functions were also needed by another pipeline, where should they live?

## Git Submission
Suggested commit:
`Complete Python Lab 4 - Pandas EDA and cleaning`
