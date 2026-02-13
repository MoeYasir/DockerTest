import math
import pytest

from hello_repo import safe_divide


def test_safe_divide_happy_path():
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)


@pytest.mark.parametrize("a,b", [(math.nan, 1), (1, math.nan), (math.inf, 1), (1, -math.inf)])
def test_safe_divide_rejects_non_finite(a, b):
    with pytest.raises(ValueError):
        safe_divide(a, b)


def test_safe_divide_type_validation():
    with pytest.raises(TypeError):
        safe_divide("1", 2)  # type: ignore[arg-type]