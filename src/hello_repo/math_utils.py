from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def safe_divide(a: Number, b: Number) -> float:
    """
    Divide a by b with basic validation.

    Rules:
    - b must not be 0
    - inputs must be finite numbers (no NaN/Inf)
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be numbers")

    a_f = float(a)
    b_f = float(b)

    if not (math.isfinite(a_f) and math.isfinite(b_f)):
        raise ValueError("a and b must be finite")

    if b_f == 0.0:
        raise ZeroDivisionError("division by zero")

    return a_f / b_f