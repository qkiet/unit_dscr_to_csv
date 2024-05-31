from helper import \
    get_line_contain_first_keyword, \
    get_value_of_field_in_unit_entry, \
    get_one_value_in_comma_separated_series_in_unit_entry


def unit_field_handler(entry: str) -> str:
    return get_value_of_field_in_unit_entry(entry, "type")


def faction_field_handler(entry: str) -> str:
    return '\"' + get_value_of_field_in_unit_entry(entry, "ownership") + '\"'


def attack_damage_field_handler(entry: str) -> str:
    return str(int(
        get_one_value_in_comma_separated_series_in_unit_entry(
            entry, field="stat_pri", index_in_series=0)))


def charge_bounus_field_handler(entry: str) -> str:
    return str(int(
        get_one_value_in_comma_separated_series_in_unit_entry(
            entry, field="stat_pri", index_in_series=1)))


class UnitCsvFieldTableEntry:
    def __init__(self, csv_field_name: str, handler) -> None:
        self.csv_field_name = csv_field_name
        self.handler = handler


# The order of this list affect the order of CSV header!
UNIT_CSV_FIELD_TABLE = [
    UnitCsvFieldTableEntry("Unit", unit_field_handler),
    UnitCsvFieldTableEntry("Faction", faction_field_handler),
    UnitCsvFieldTableEntry("Attack", attack_damage_field_handler),
    UnitCsvFieldTableEntry("Charge Bounus", charge_bounus_field_handler),
    # Add new CSV column and its handler here
]
