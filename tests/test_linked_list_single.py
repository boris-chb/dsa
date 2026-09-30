import pytest

from dsa.data_structures.linked_list_single import LinkedList

CASES = [
    (
        [
            ("insertHead", 1),
            ("insertTail", 2),
            ("insertHead", 0),
            ("remove", 1),
            ("getValues",),
        ],
        [None, None, None, True, [0, 2]],
    ),
    (
        [("insertHead", 1), ("insertHead", 2), ("get", 5)],
        [None, None, -1],
    ),
]


@pytest.mark.parametrize("ops,expected", CASES)
def test_linked_list(ops, expected):
    ll = LinkedList()
    actual = [getattr(ll, op)(*args) for op, *args in ops]
    assert actual == expected
