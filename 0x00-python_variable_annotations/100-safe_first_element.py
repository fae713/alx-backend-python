#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the iterable if it exists;
    otherwise, returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
