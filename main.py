from unit_entry_parser import UnitEntryParser
from unit_csv_field_table import UNIT_CSV_FIELD_TABLE

# Unit entry look like below
demo_entry = \
    "type             Lettish Crossbowmen\r\n" \
    "dictionary       Lettish_Crossbowmen      ; Latvian Crossbowmen, l\r\n" \
    "category         infantry\r\n" \
    "class            skirmish\r\n" \
    "ownership        byzantium\r\n" \




def get_first_unit_entry_and_move_next_entry(big_text: str, start_index=0) -> tuple[str, int]:
    # It always begin with keyword "type"
    first_index = big_text.find("type", start_index)
    if first_index == -1:
        return ("", -1)
    end_index = big_text.find("\n\n", first_index)
    return (big_text[first_index:end_index], end_index)


def parse_entire_unit_entry(unit_entry: str) -> str:
    row_value_list = []
    for _, entry in enumerate(UNIT_CSV_FIELD_TABLE):
        parser = UnitEntryParser(
            csv_field=entry.csv_field_name, parse_handler=entry.handler)
        parser.read_unit_entry(demo_entry)
        csv_value = parser.get_field_value()
        row_value_list.append(csv_value)
    return ",".join(row_value_list)


output_file.write(parse_entire_unit_entry(unit_entry=demo_entry)+"\n")
# Should output followng in "foo" csv file
# Unit,Faction
# Lettish Crossbowmen,byzantium
#
output_file.close()
