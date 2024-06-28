#!/usr/bin/env python3
"""
Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the multiplier.
    """
    def float_multipier(value: float) -> float:
        return value * multiplier
    return float_multipier
