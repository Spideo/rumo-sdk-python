import pytest

from template.add import add


def test_basic_add():
    assert add(2, 2) == 4


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 1, 1),
        (-2, 1, -1),
        ("aa", "bb", "aabb"),
        ("", "a", "a"),
        ([], [1, 2], [1, 2]),
        (["a"], [1, 2], ["a", 1, 2]),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b", [("ab", 42), ([1], 42), ("aaa", None), (True, "42"), ([], 42)]
)
def test_add_incompatible_type(a, b):
    with pytest.raises(TypeError):
        add(a, b)
