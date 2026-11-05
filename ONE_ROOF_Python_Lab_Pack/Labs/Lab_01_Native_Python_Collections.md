# Lab 1 — Raw Operational Data Inspection

## Business Scenario
Gate Operations has sent you a Python collection containing recent gate transactions.

```python
gate_transactions = [
    {
        "TransactionID": "GT1001",
        "ContainerNumber": " MSKU 100001 ",
        "GateDirection": "in",
        "TruckNumber": " TRK 101 ",
        "GrossWeightKg": 28500
    },
    {
        "TransactionID": "GT1002",
        "ContainerNumber": "CMAU200002",
        "GateDirection": "OUT",
        "TruckNumber": None,
        "GrossWeightKg": 17200
    },
    {
        "TransactionID": "GT1003",
        "ContainerNumber": " tghu 300003 ",
        "GateDirection": "IN",
        "TruckNumber": "TRK103",
        "GrossWeightKg": 32000
    }
]


## Business Requirements
Produce a cleaned version where:
- ContainerNumber has no unnecessary spaces and is uppercase.
- GateDirection is uppercase.
- Missing TruckNumber becomes `NO TRUCK RECORDED`.
- TruckNumber contains no unnecessary spaces.
- GrossWeightKg is also returned as GrossWeightTons.
- WeightClass is LIGHT below 10 tons, MEDIUM from 10–25 tons, HEAVY above 25 tons.

## Required Output
Each record must contain:
- TransactionID
- ContainerNumber
- GateDirection
- TruckNumber
- GrossWeightKg
- GrossWeightTons
- WeightClass


## Engineering Structure Expectation
Where appropriate:
- move repeated logic into functions;
- give functions clear names based on what they do;
- create your own `.py` module when multiple parts of the solution should reuse the same logic;
- import your own functions rather than copying them between scripts.

Do not force a function or module where a few simple lines are clearer.


## Engineering Review
1. Why did you not change TransactionID? It met the business requirement.
2. What object type was each transaction? Each Transaction is a string data type, except the GrossWeight which was integer.
3. Which operations were string methods? The replace, Upper, and Split.
4. Which parts of your solution would benefit from becoming functions? The parts where i needed to rename the columns, and do some cleaning.

## Git Submission
Suggested commit:
`Complete Python Lab 1 - native collection cleaning`


- ContainerNumber has no unnecessary spaces and is uppercase.
- GateDirection is uppercase.
- Missing TruckNumber becomes `NO TRUCK RECORDED`.
- TruckNumber contains no unnecessary spaces.
- GrossWeightKg is also returned as GrossWeightTons.
- WeightClass is LIGHT below 10 tons, MEDIUM from 10–25 tons, HEAVY above 25 tons.

### First Approach, Create a function that does this native cleaning for just the whole list

def native_cleaning(gate_transactions):
    Cleaned_Collection = []
    for transactions in gate_transactions:
        # Clean Container Number
        if isinstance(transactions['ContainerNumber'], str):
        transactions['ContainerNumber'] = transactions['ContainerNumber'].strip().replace(" ", "").upper()

        #Standardize Gate Direction
        if isinstance(transactions['GateDirection'], str):
        transactions['GateDirection'] = transactions['GateDirection'].upper()

        # Missing TruckNumber becomes `NO TRUCK RECORDED`, and TruckNumber contains no unnecessary spaces.
        truck_number = transaction['TruckNumber']
        if truck_number is None or truck_number == '':
            transaction['TruckNumber'] = 'NO TRUCK RECORDED'
        else:
            transaction['TruckNumber'] = truck_number.strip()


        # Convert GrossWeightKg to GrossWeightTons
        gross_weight = transaction['GrossWeightKg']
        transaction['GrossWeightTons'] = float(gross_weight) / 1000

        #WeightClass is LIGHT below 10 tons, MEDIUM from 10–25 tons, HEAVY above 25 tons.
        if transaction['GrossWeightTons'] is not None and transaction['GrossWeightTons'] < 10:
            transaction['WeightClass'] = 'LIGHT'
        elif transaction['GrossWeightTons'] is not None and transaction['GrossWeightTons'] >= 10 and transaction['GrossWeightTons'] <= 25:
            transaction['WeightClass'] = 'MEDIUM'
 
        else:
            transaction['WeightClass'] = 'HEAVY'

        Cleaned_Collection.append(transactions)


    return Cleaned_Collection

Reusable_func = native_cleaning(gate_transactions)
print(Reusable_func)


        

