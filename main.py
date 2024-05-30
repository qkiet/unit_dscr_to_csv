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

WANTED_CSV_FIELD = ["Unit", "Faction"]
FIELD_HANDLER = [unit_field_handler, faction_field_handler]

output_file = open("foo.csv", "w+")
csv_header = ",".join(WANTED_CSV_FIELD) + "\n"
output_file.write(csv_header)

row_value_list = []
for i in range(0, len(WANTED_CSV_FIELD)):
    parser = UnitEntryParser(csv_field=WANTED_CSV_FIELD[i], parse_handler=FIELD_HANDLER[i])
    parser.read_unit_entry(demo_entry)
    csv_value = parser.get_field_value()
    row_value_list.append(csv_value)
row_string = ",".join(row_value_list) + "\n"
output_file.write(row_string)
## Should output followng in "foo" csv file
# Unit,Faction
# Lettish Crossbowmen,byzantium
#
output_file.close()
