#!/usr/bin/env python3
"""
This module contains a coroutine that will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers defined in 0-aync_genrator.
"""

from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    An asynchronous coroutine that yields random floating number from 0 to 10.
    """

    return [i async for i in async_generator()]
