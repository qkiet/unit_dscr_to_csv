def get_line_contain_first_keyword(
        multi_line_str: str,
        first_keyword: str) -> str:
    found_index = multi_line_str.find(first_keyword)
    if found_index == -1:
        return ""
    substr = multi_line_str[found_index:]
    return substr.split("\n")[0]


def get_value_of_field_in_unit_entry(
        multi_line_str: str,
        field: str) -> str:
    try:
        wanted_line = get_line_contain_first_keyword(multi_line_str, field)
    except Exception as e:
        raise Exception("Encounter fatal exception") from e
    else:
        if wanted_line == "":
            return ""
    return wanted_line.split(maxsplit=1)[1]


def get_one_integer_in_series_in_unit_entry(
        multi_line_str: str,
        field: str,
        index_in_series) -> str:
    series = get_value_of_field_in_unit_entry(multi_line_str, field)
    integer_value = int(series.split(",")[index_in_series])
    return str(integer_value)
