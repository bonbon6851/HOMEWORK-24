from typing import Callable

from utils import read_file, filter_query, map_query, unique_query, sorted_query, limit_query, regex_query


CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sorted_query,
    'limit': limit_query,
    'regex': regex_query
}


def build_query(cmd: str, value: str | int, file_name: str, data: list | None) -> list:
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    func = CMD_TO_FUNCTION[cmd]
    result = func(value=value, data=prepared_data)

    return list(result)
