import pytest

from rumo_sdk.utils import FilterOperatorType, RumoFilters, batched


@pytest.mark.parametrize(
    "iterable, n, output",
    [
        ("ABCDEFG", 3, [("A", "B", "C"), ("D", "E", "F"), ("G",)]),
        ("ABCDEFG", 2, [("A", "B"), ("C", "D"), ("E", "F"), ("G",)]),
        ("ABCDEFG", 1, [("A",), ("B",), ("C",), ("D",), ("E",), ("F",), ("G",)]),
    ],
)
def test_batched(iterable, n, output):
    assert list(batched(iterable, n)) == output


@pytest.mark.parametrize(
    "iterable, n, exception",
    [
        ("ABCDEFG", 0, ValueError),
        ("ABCDEFG", -1, ValueError),
        ("ABCDEFG", "toto", TypeError),
        (None, None, TypeError),
        ("ABCDEFG", None, TypeError),
        (12345, 3, TypeError),
    ],
)
def test_bad_input(iterable, n, exception):
    with pytest.raises(exception):
        list(batched(iterable, n=n))


@pytest.mark.parametrize(
    "filters, operator, expected",
    [
        (
            {"f_a": ["v_a"]},
            FilterOperatorType.OR,
            {"filters": ["f_a:v_a"], "filterOperator": "OR"},
        ),
        (
            {"f_a": ["v_a", "v_b"]},
            FilterOperatorType.AND,
            {"filters": ["f_a:v_a,v_b"], "filterOperator": "AND"},
        ),
        (
            {"f_a": ["v_a", "v_b"], "f_b": ["v_c"]},
            FilterOperatorType.AND,
            {"filters": ["f_a:v_a,v_b", "f_b:v_c"], "filterOperator": "AND"},
        ),
    ],
)
def test_format_filters(filters, operator, expected):
    rumo_filters = RumoFilters(filters, operator)
    assert rumo_filters.format_filters_to_query_params() == expected
