# ONE-ROOF PortOps Pipeline
from portops_utils_main import native_cleaning
# Orchestrate your pipeline here.
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

       

Reusable_func = native_cleaning(gate_transactions)
print(Reusable_func)


