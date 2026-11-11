"""Reusable PortOps pipeline functions."""
# Add reusable functions here.

from ast import Return


def native_cleaning(gate_transactions):
    Cleaned_Collection = []
    for transactions in gate_transactions:
        transactions = transactions.copy()
        # Clean Container Number
        if isinstance(transactions['ContainerNumber'], str):
            transactions['ContainerNumber'] = transactions['ContainerNumber'].strip().replace(" ", "").upper()

        #Standardize Gate Direction
        if isinstance(transactions['GateDirection'], str):
            transactions['GateDirection'] = transactions['GateDirection'].upper()

        # Missing TruckNumber becomes `NO TRUCK RECORDED`, and TruckNumber contains no unnecessary spaces.
        truck_number = transactions['TruckNumber']
        if truck_number is None or truck_number == '':
            transactions['TruckNumber'] = 'NO TRUCK RECORDED'
        else:
            transactions['TruckNumber'] = truck_number.strip()


      # Convert GrossWeightKg to GrossWeightTons
        gross_weight = transactions['GrossWeightKg']

        try:
            if gross_weight == '' or gross_weight is None:
                transactions['GrossWeightTons'] = None
            else:
                transactions['GrossWeightTons'] = float(gross_weight) / 1000

        except ValueError:
            transactions['GrossWeightTons'] = None


        #WeightClass is LIGHT below 10 tons, MEDIUM from 10–25 tons, HEAVY above 25 tons.
        if transactions['GrossWeightTons'] is not None and transactions['GrossWeightTons'] < 10:
            transactions['WeightClass'] = 'LIGHT'
        elif transactions['GrossWeightTons'] is not None and transactions['GrossWeightTons'] >= 10 and transactions['GrossWeightTons'] <= 25:
            transactions['WeightClass'] = 'MEDIUM'
 
        else:
            transactions['WeightClass'] = 'HEAVY'

        Cleaned_Collection.append(transactions)


    return Cleaned_Collection


#Functions for Records Receieved
def records_received(dirty_data):
    # Count the number of records received
    records_received = 0
    for records in dirty_data:
        records_received += 1
    return records_received

#Identify records with missing TransactionID
# def identify_missing_transaction_id(dirty_data):
#     missing_transaction_id_records = []
#     for record in dirty_data:
#         if not record.get('TransactionID'):
#             missing_transaction_id_records.append(record)
#     return missing_transaction_id_records

def identify_missing_transaction_id(dirty_data):
    missing_transaction_id_records = []
    for record in dirty_data:
        if record['TransactionID'] is None or record['TransactionID'] == '':
            missing_transaction_id_records.append(record)
    return missing_transaction_id_records

#Identify records with missing TruckNumber
def identify_missing_truck_number(dirty_data):
    missing_truck_number_records = []
    for record in dirty_data:
        if record['TruckNumber'] is None or record['TruckNumber'].strip() == '':
            missing_truck_number_records.append(record)
    return missing_truck_number_records

#identify invalid Gate Direction value
def identify_invalid_gate_direction(dirty_data):
    Invalid_gate_direction = []

    for v in dirty_data:
        if v['GateDirection'] is None or v['GateDirection'] == '':
            Invalid_gate_direction.append(v)

        else:
            if v['GateDirection'].upper() not in ['IN', 'OUT']:
                Invalid_gate_direction.append(v)

    return Invalid_gate_direction

#identify GrossWeightKg values that cannot be treated as numbers
def invalid_gross_weight(dirty_data):
    invalid_gross_weight_records = []
    for record in dirty_data:
        try:
            float(record['GrossWeightKg'])
        except (ValueError, TypeError):
            invalid_gross_weight_records.append(record)
    return invalid_gross_weight_records


#Preserve invalid records rather than silently discarding them.

def Preserved_records(dirty_data):
    Total_invalid_records = []
    Total_invalid_records.append(identify_missing_transaction_id(dirty_data))
    Total_invalid_records.append(identify_missing_truck_number(dirty_data))
    Total_invalid_records.append(identify_invalid_gate_direction(dirty_data))
    Total_invalid_records.append(invalid_gross_weight(dirty_data))
    return Total_invalid_records


def valid_records(dirty_data):
    valid_records = []
    for record in dirty_data:
        if (record not in identify_missing_transaction_id(dirty_data) and
            record not in identify_missing_truck_number(dirty_data) and
            record not in identify_invalid_gate_direction(dirty_data) and
            record not in invalid_gross_weight(dirty_data)):
            valid_records.append(record)
    return valid_records


