#!/usr/bin/env python3

"""
This module demonstrates an asynchronous routine named wait_n.
It spawns wait_random n times with a specified max_delay.
It collects the delays in a list and sorts them in ascending order.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

# from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Parameters:
    1. n (int): The number of times to spawn wait_random.
    2. max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    1. list: A list of delays in ascending order.
    """

    delays = []

    # Spawn wait_random n times
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    sorted_delays = sorted(delays)

    return sorted_delays
