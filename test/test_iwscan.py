import pytest
from typing import NamedTuple

from comitup.iwscan import decode_x


class Case(NamedTuple):
    instr: str
    outstr: str


@pytest.mark.parametrize(
    "case",
    [
        Case("but", "but"),
        Case("b\xc3\xbct", "büt"),
        Case("b\x00\x00t", "b\x00\x00t"),
    ],
)
def test_decode_x(case):
    assert decode_x(case.instr) == case.outstr
