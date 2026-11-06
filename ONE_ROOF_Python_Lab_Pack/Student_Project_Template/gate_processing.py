from portops_utils_main import native_cleaning, records_received,identify_missing_transaction_id, identify_missing_truck_number
from portops_utils_main import identify_invalid_gate_direction, invalid_gross_weight
#from pathlib import path
import csv
import logging

logging.basicConfig(
    filename="C:\\Users\\willi\\OneDrive\\Documents\\DATA_ENGINEERING\\PYTHON_PROJECT\\ONE_ROOF_Python_Lab_Pack\\Logs\\etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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
     

Reusable_function = native_cleaning(gate_transactions)
print(Reusable_function)

#Lab 3 file ingestion and processing pipeline
Dirty_data = "C:/Users/willi/OneDrive/Documents/DATA_ENGINEERING/PYTHON_PROJECT/ONE_ROOF_Python_Lab_Pack/Data/PortOps_Gate_Transactions_Dirty.csv"
try:
    with open(Dirty_data, "r") as f:
        # Process the dirty data
        csv_reader = csv.DictReader(f)
        all_records = [] # I need to store all the records in a list to count the number of records received.
        for val in csv_reader:
            all_records.append(val) # Store all the records in a list to count the number of records received.
        Total_records_received = records_received(all_records) #created a function to count the number of records received in the dirty data file.
        print(Total_records_received)
        logging.info(f"Rows_Read: {Total_records_received}")
except FileNotFoundError:
    print(f"File not found: {Dirty_data}")


# identify records with missing TransactionID
try:
    #Create a list to store the records with missing TransactionID
    list_of_missing_transaction_id_records = []

    #Call the function to identify records with missing TransactionID, and store the result in a variable
    Missing_transaction_id_records = identify_missing_transaction_id(all_records) 
    print(f"Records with missing TransactionID: {len(Missing_transaction_id_records)}")
    print(f"Records with missing TransactionID: {Missing_transaction_id_records}")

    #Iterate through the list of records with missing TransactionID and print each record, and append each record to the list_of_missing_transaction_id_records
    for record in Missing_transaction_id_records:
        print(f"Missing TransactionID Record: {record}")
        list_of_missing_transaction_id_records.append(record)
        #Log the records with missing TransactionID
    logging.info(f"Records with missing TransactionID: {list_of_missing_transaction_id_records}")
except Exception as e:
    print(f"Error occurred while identifying missing transaction IDs: {e}")
    logging.error(f"Error occurred while identifying missing transaction IDs: {e}")

# Refined Version
try:
    #Create a list to store the records with missing TransactionID
    
    #Call the function to identify records with missing TransactionID, and store the result in a variable
    Missing_transaction_id_records = identify_missing_transaction_id(all_records) 
    print(f"Records with missing TransactionID: {len(Missing_transaction_id_records)}")
    print(f"Records with missing TransactionID: {Missing_transaction_id_records}")

    logging.info(f"Records with missing TransactionID: {Missing_transaction_id_records}")
except Exception as e:
    print(f"Error occurred while identifying missing transaction IDs: {e}")
    logging.error(f"Error occurred while identifying missing transaction IDs: {e}")


 # identify records with missing TruckNumber
try:
    Missing_truck_number_records = identify_missing_truck_number(all_records)
    print(f"Records with missing TruckNumber: {len(Missing_truck_number_records)}")
    logging.warning(f"Records with missing TruckNumber: {len(Missing_truck_number_records)}")
except Exception as e:
    print(f"Error occurred while identifying missing truck numbers: {e}")
    logging.error(f"Error occurred while identifying missing truck numbers: {e}")


# Identify invalid GateDirection values
try:
    Invalid_gate_direction_records = identify_invalid_gate_direction(all_records)
    print(f"Records with invalid GateDirection: {len(Invalid_gate_direction_records)}")
    logging.warning(f"Records with invalid GateDirection: {len(Invalid_gate_direction_records)}")
except Exception as e:
    print(f"Error occurred while identifying invalid gate directions: {e}")
    logging.error(f"Error occurred while identifying invalid gate directions: {e}")

try:
    Invalid_gross_weight_records = invalid_gross_weight(all_records)
    print(f"Records with invalid GrossWeightKg: {len(Invalid_gross_weight_records)}")
    logging.warning(f"Records with invalid GrossWeightKg: {len(Invalid_gross_weight_records)}")
except Exception as e:
    print(f"Error occurred while identifying invalid GrossWeightKg: {e}")
    logging.error(f"Error occurred while identifying invalid GrossWeightKg: {e}")