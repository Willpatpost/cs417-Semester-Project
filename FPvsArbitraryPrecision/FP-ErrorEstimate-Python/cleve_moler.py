#! /usr/bin/env python3

import math
import typing

from decimal import (Decimal)
from fractions import Fraction

D_ONE = Decimal(1.0)

def estimate_precision_float():
    a = (4.0 / 3.0)
    b = a - 1.0
    c = b + b + b

    return math.fabs(c - 1.0)


def estimate_precision_float_type_hints() -> float:
    a = (4.0 / 3.0)  # type: float
    b = a - 1.0      # type: float
    c = b + b + b    # type: float

    return math.fabs(c - 1.0)


def estimate_precision_decimal() -> Decimal:
    a = Decimal(4.0) / Decimal(3.0)
    b = a - Decimal(1.0)
    c = b + b + b

    return abs(D_ONE - c)

