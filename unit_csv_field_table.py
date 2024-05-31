from helper import get_line_contain_first_keyword, get_value_of_field_in_unit_entry

def unit_field_handler(entry: str) -> str:
    return get_value_of_field_in_unit_entry(entry, "type")

def faction_field_handler(entry: str) -> str:
    return get_value_of_field_in_unit_entry(entry, "ownership")

class UnitCsvFieldTableEntry:
    def __init__(self, csv_field_name: str, handler) -> None:
        self.csv_field_name = csv_field_name
        self.handler = handler
        

UNIT_CSV_FIELD_TABLE = [
    UnitCsvFieldTableEntry("Unit", unit_field_handler),
    UnitCsvFieldTableEntry("Faction", faction_field_handler)
]
