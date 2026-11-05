"""Reusable PortOps pipeline functions."""
# Add reusable functions here.

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
        truck_number = transactions['TruckNumber']
        if truck_number is None or truck_number == '':
            transactions['TruckNumber'] = 'NO TRUCK RECORDED'
        else:
            transactions['TruckNumber'] = truck_number.strip()


        # Convert GrossWeightKg to GrossWeightTons
        gross_weight = transactions['GrossWeightKg']
        transactions['GrossWeightTons'] = float(gross_weight) / 1000

        #WeightClass is LIGHT below 10 tons, MEDIUM from 10–25 tons, HEAVY above 25 tons.
        if transactions['GrossWeightTons'] is not None and transactions['GrossWeightTons'] < 10:
            transactions['WeightClass'] = 'LIGHT'
        elif transactions['GrossWeightTons'] is not None and transactions['GrossWeightTons'] >= 10 and transactions['GrossWeightTons'] <= 25:
            transactions['WeightClass'] = 'MEDIUM'
 
        else:
            transactions['WeightClass'] = 'HEAVY'

        Cleaned_Collection.append(transactions)


    return Cleaned_Collection




