from collections.abc import Generator, Iterable
from enum import Enum
from itertools import islice


def batched(iterable: Iterable, n: int) -> Generator:
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


class FilterOperatorType(Enum):
    AND = "AND"
    OR = "OR"


class ItemType(Enum):
    SINGLE = "single"
    PARENT = "parent"
    CHILD = "child"


class RumoFilters:
    FilterType = dict[str, list[str]]

    def __init__(self, filters: FilterType, filter_operator: FilterOperatorType):
        self.filters = filters
        self.filter_operator = filter_operator

    def format_filters_to_query_params(self) -> dict:
        filters = []
        for key, value in self.filters.items():
            filters.append(f"{key}:{','.join([elem for elem in value])}")
        return {"filters": filters, "filterOperator": self.filter_operator.value}
