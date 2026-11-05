From python_session.py import double_container_column_cleaner



def kg_to_tons(weight_kg):
    weight_tons = weight_kg / 1000
    return weight_tons

def single_container_column_cleaner(value):
    if value is None:
        return None
    return value.strip().replace(" ", "").upper()