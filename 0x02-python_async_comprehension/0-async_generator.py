#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
It will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    This is an async coroutine that yields random floating numbers from 0 - 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
