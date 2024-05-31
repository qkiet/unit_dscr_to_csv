from unit_entry_parser import UnitEntryParser

## Unit entry look like below
demo_entry = \
    "type             Lettish Crossbowmen\r\n" \
    "dictionary       Lettish_Crossbowmen      ; Latvian Crossbowmen, l\r\n" \
    "category         infantry\r\n" \
    "class            skirmish\r\n" \
    "ownership        byzantium\r\n" \

def get_line_contain_first_keyword(
        multi_line_str: str,
        first_keyword: str) -> str:
    found_index = multi_line_str.find(first_keyword)
    substr = multi_line_str[found_index:]
    return substr.split("\r\n")[0]

def get_value_of_field_in_unit_entry(
        multi_line_str: str,
        field: str) -> str:
    wanted_line = get_line_contain_first_keyword(multi_line_str, field)
    return wanted_line.split(maxsplit=1)[1]

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

output_file = open("foo.csv", "w+")
csv_header = ",".join(entry.csv_field_name for entry in UNIT_CSV_FIELD_TABLE) + "\n"
output_file.write(csv_header)

def parse_entire_unit_entry(unit_entry: str) -> str:
    row_value_list = []
    for _, entry  in enumerate(UNIT_CSV_FIELD_TABLE):
        parser = UnitEntryParser(csv_field=entry.csv_field_name, parse_handler=entry.handler)
        parser.read_unit_entry(demo_entry)
        csv_value = parser.get_field_value()
        row_value_list.append(csv_value)
    return ",".join(row_value_list)

output_file.write(parse_entire_unit_entry(unit_entry=demo_entry)+"\n")
## Should output followng in "foo" csv file
# Unit,Faction
# Lettish Crossbowmen,byzantium
#
output_file.close()
