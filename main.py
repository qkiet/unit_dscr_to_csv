from unit_entry_parser import UnitEntryParser
from unit_csv_field_table import UNIT_CSV_FIELD_TABLE


def get_first_unit_entry_and_move_next_entry(big_text: str, start_index=0) -> tuple[str, int]:
    # It always begin with keyword "type"
    first_index = big_text.find("type", start_index)
    if first_index == -1:
        return ("", -1)
    end_index = big_text.find("\n\n\n", first_index)
    return (big_text[first_index:end_index], end_index)


def parse_entire_unit_entry(unit_entry: str) -> str:
    row_value_list = []
    for _, entry in enumerate(UNIT_CSV_FIELD_TABLE):
        parser = UnitEntryParser(
            csv_field=entry.csv_field_name, parse_handler=entry.handler)
        parser.read_unit_entry(unit_entry)
        csv_value = parser.get_field_value()
        row_value_list.append(csv_value)
    return ",".join(row_value_list)


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


def parse_entire_txt(txt: str) -> list[str]:
    start_pos = 0
    csv_row_list = []
    while True:
        my_unit_entry, next_index = get_first_unit_entry_and_move_next_entry(
            txt, start_index=start_pos)
        if not my_unit_entry == "":
            parsed_csv_row = parse_entire_unit_entry(my_unit_entry)
            csv_row_list.append(parsed_csv_row)
        if next_index == -1:
            return csv_row_list
        start_pos = next_index


def main():
    in_file = open("export_descr_unit.txt", "r", encoding="utf-8")
    big_text = in_file.read()
    in_file.close()

    out_file = open("output.csv", "w+", encoding="utf-8")
    list_csv_header = [entry.csv_field_name for entry in UNIT_CSV_FIELD_TABLE]
    csv_header = ",".join(list_csv_header)
    out_file.write(csv_header + "\n")

    clean_up_text = remove_line_comment(big_text)
    csv_rows = parse_entire_txt(clean_up_text)
    csv_content = "\n".join(csv_rows)
    out_file.write(csv_content)
    out_file.close()


if __name__ == "__main__":
    main()
