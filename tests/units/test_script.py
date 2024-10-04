import pytest
import mylyric.lib.lyric_module as invoke_cpp


def test_calculate():
    a = 10
    b = 20
    result = invoke_cpp.simple_cpp_function(a, b)
    assert result == 30