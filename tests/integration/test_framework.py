import pytest
from mylyric.framework import sample_function


def test_calculate():
    assert sample_function() == 8
    