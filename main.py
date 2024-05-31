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



DEMO_TXT = \
    """
type             baghlah
dictionary       baghlah      ; Baghlah
category         ship
class            light
voice_type       Light
soldier          Peasants, 50, 0, 1
ship             heavy warship
attributes       sea_faring, can_withdraw
formation        50, 50, 75, 75, 1, square
stat_health      1, 1
stat_pri         18, 0, no, 0, 0, melee, melee_simple, slashing, none, 0, 1
stat_pri_attr    no
stat_sec         0, 0, no, 0, 0, no, melee_simple, blunt, none, 0, 1
stat_sec_attr    no
stat_pri_armour  0, 22, 0, flesh
stat_sec_armour  0, 0, flesh
stat_heat        0
stat_ground      0, 0, 0, 0
stat_mental      15, normal, trained
stat_charge_dist 20
stat_fire_delay  0
stat_food        60, 300
stat_cost        1, 1190, 150, 250, 250, 1150, 4, 280
armour_ug_levels 0
armour_ug_models Peasants
ownership        egypt, turks, moors, kwarezm
recruit_priority_offset    -45 


type             caravel
dictionary       caravel      ; Caravel
category         ship
class            light
voice_type       Light
soldier          Peasants, 30, 0, 1
ship             heavy warship
attributes       sea_faring, can_withdraw
formation        50, 50, 75, 75, 1, square
stat_health      1, 1
stat_pri         15, 0, no, 0, 0, melee, melee_simple, slashing, none, 0, 1
stat_pri_attr    no
stat_sec         0, 0, no, 0, 0, no, melee_simple, blunt, none, 0, 1
stat_sec_attr    no
stat_pri_armour  0, 15, 0, flesh
stat_sec_armour  0, 0, flesh
stat_heat        0
stat_ground      0, 0, 0, 0
stat_mental      14, normal, trained
stat_charge_dist 20
stat_fire_delay  0
stat_food        60, 300
stat_cost        1, 890, 275, 200, 200, 850, 4, 210
armour_ug_levels 0
armour_ug_models Peasants
ownership        portugal, spain, aragon
recruit_priority_offset    -45 


type             carrack
dictionary       carrack      ; Carrack
category         ship
class            light
voice_type       Light
soldier          Peasants, 50, 0, 1
ship             heavy warship
attributes       sea_faring, can_withdraw
formation        50, 50, 75, 75, 1, square
stat_health      1, 1
stat_pri         30, 0, no, 0, 0, melee, melee_simple, slashing, none, 0, 1
stat_pri_attr    no
stat_sec         0, 0, no, 0, 0, no, melee_simple, blunt, none, 0, 1
stat_sec_attr    no
stat_pri_armour  0, 30, 0, flesh
stat_sec_armour  0, 0, flesh
stat_heat        0
stat_ground      0, 0, 0, 0
stat_mental      14, normal, trained
stat_charge_dist 20
stat_fire_delay  0
stat_food        60, 300
stat_cost        1, 1540, 350, 250, 250, 1500, 4, 370
armour_ug_levels 0
armour_ug_models Peasants
ownership        northern_european, venice, sicily, milan, papal_states, eastern_european, greek
recruit_priority_offset    -45 
"""


def remove_line_comment(txt: str, line_comment_precedor=";") -> str:
    tmp = txt
    while True:
        found_index = tmp.find(line_comment_precedor)
        if found_index == -1:
            return tmp
        end_of_line_index = tmp.find("\n", found_index)
        # If end of line not found means this is EOF
        if end_of_line_index == -1:
            end_of_line_index = len(tmp)
        tmp = tmp[:found_index] + tmp[end_of_line_index:]


def parse_entire_txt(txt: str):
    start_pos = 0
    while True:
        my_unit_entry, next_index = get_first_unit_entry_and_move_next_entry(
            txt, start_index=start_pos)
        parsed_csv_row = parse_entire_unit_entry(my_unit_entry)
        print(parsed_csv_row)
        if next_index == -1:
            break
        start_pos = next_index


parse_entire_txt(DEMO_TXT)
