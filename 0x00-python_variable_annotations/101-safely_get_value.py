#!/usr/bin/env python3
"""
More involved type annotations
"""

from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T],
                     key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """
    Returns the value for the given key if it exists
    in the dictionary, otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
