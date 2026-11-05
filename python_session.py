name_1 =' Johnson Jay '
container_list = ['msk122','msk1234','msk234567']
dict = {'Student_ID': '1', 'Student_Name': 'Johnsons', 'Student_Age': '20'}
set = {'Student_ID', 'Student_Name', 'Student_Age'}
tuple = ('Student_ID', 'Student_Name', 'Student_Age')


#String methods
# name_caps = name_1.upper()
# print(name_caps)
# name_lower = name_1.lower()
# print(name_lower)
# name_strip = name_1.strip()
# print(name_strip)
# name_replace = name_1.replace(' ', 'Mr. ')
# print(name_replace)

# name_j_count = name_1.count('J')
# print(name_j_count)

# List methods

container_list.append('msk345')
print(container_list)

#dict methods
dict.update({'Student_Age': '21'})
print(dict)

dict_items = dict.items()
print(dict_items)

#f-string methods
# name = 'Segun'
# age = 35
# print(f"Hello, my name is {name} and I am {age} years old.")

# raw_container = " MSC 123456 " 
# new_value ="MSC123456"
# raw_container = " MSC 123456"
# new_raw_container = raw_container.strip().replace(" ", "")
# print(new_raw_container)

list_of_container = [' MSKU 10000 ', 'cmau200002', ' THGU 300003 ']

# string_number = '10'
# type(string_number)
# for container in list_of_container:
#     new_container = container.strip().replace(" ", "").upper()    
#     print(new_container)

transactions_data = [
    {'container_number': 'MSKU 10000', 'transaction_type': 'Import', 'transaction_date': '2023-01-01'},
    {'container_number': 'CMAU 200002', 'transaction_type': 'Export', 'transaction_date': '2023-02-01'},
    {'container_number': 'THGU 300003', 'transaction_type': 'Import',   'transaction_date': '2023-03-01'}
    ]

for transaction in transactions_data:
        print(f"Container Number: {transaction['container_number']},\n"
            f"Transaction Type: {transaction['transaction_type']},\n"
            f"Transaction Date: {transaction['transaction_date']}")

# Function to check if a container number exists in the transactions data
from portops_utils import kg_to_tons, single_container_column_cleaner


kg_weight = 5000
result_in_tons = kg_to_tons(kg_weight)
print(f"{kg_weight} kg is equal to {result_in_tons} tons.")


cleaned_container = single_container_column_cleaner(list_of_container[2])
print(cleaned_container)



def double_container_column_cleaner(list_of_container):
    cleaned_containers = []
    for container in list_of_container:
        cleaned_container = container.strip().replace(" ", "").upper()
        cleaned_containers.append(cleaned_container)
    return cleaned_containers


cleaned_containers = double_container_column_cleaner(list_of_container)
print(cleaned_containers)


From Pathlib import Path


Transactions = Path('C:\\Users\\willi\\OneDrive\\Documents\\DATA_ENGINEERING\\PYTHON_PROJECT\\PortOps_Gate_Transactions_Dirty.csv')
