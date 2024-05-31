def get_line_contain_first_keyword(
        multi_line_str: str,
        first_keyword: str) -> str:
    found_index = multi_line_str.find(first_keyword)
    substr = multi_line_str[found_index:]
    return substr.split("\n")[0]


def get_value_of_field_in_unit_entry(
        multi_line_str: str,
        field: str) -> str:
    wanted_line = get_line_contain_first_keyword(multi_line_str, field)
    return wanted_line.split(maxsplit=1)[1]
