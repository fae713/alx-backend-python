#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine named wait_random..
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Params:
    - max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    - float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(wait_random(5))
