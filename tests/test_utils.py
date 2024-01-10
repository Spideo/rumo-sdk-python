import pytest

from rumo_sdk.utils import batched


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
