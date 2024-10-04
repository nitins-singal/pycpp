import pytest
import mylyric.lib.lyric_module as invoke_cpp
from mylyric.script import calculate


def test_calculate():
    assert calculate() == 15