from unit_entry_parser import UnitEntryParser
from unit_csv_field_table import UNIT_CSV_FIELD_TABLE

## Unit entry look like below
demo_entry = \
    "type             Lettish Crossbowmen\r\n" \
    "dictionary       Lettish_Crossbowmen      ; Latvian Crossbowmen, l\r\n" \
    "category         infantry\r\n" \
    "class            skirmish\r\n" \
    "ownership        byzantium\r\n" \



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
