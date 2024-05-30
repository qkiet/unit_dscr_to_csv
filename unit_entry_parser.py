class UnitEntryParser:
    def __init__(
        self,
        csv_field: str,
        # function that has form parse_handler(unit_entry: str) -> str
        parse_handler,
    ):
        self.csv_field = csv_field
        self.unit_entry = None
        self.parse_handler = parse_handler

    def read_unit_entry(self, entry: str) -> None:
        self.unit_entry = entry

    def get_field_value(self) -> str:
        if self.unit_entry is not None:
            return self.parse_handler(self.unit_entry)
        else:
            raise ValueError("Expect unit entry not None")
