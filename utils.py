from typing import Iterable
import re


def read_file(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def filter_query(value: str, data: Iterable[str]) -> filter:
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]) -> map:
    col_number = int(value)
    return map(lambda x: x.split(" ")[col_number], data)


def unique_query(data: str, *args, **kwargs) -> set:
    return set(data)


def sorted_query(value: str, data: Iterable[str]) -> list:
    reverse: bool = value == 'desk'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> list:
    limit = int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterable[str]) -> list:
    regex = re.compile(value)
    result: list = []
    for item in data:
        if regex.findall(item):
            result.append(item)
    return result
