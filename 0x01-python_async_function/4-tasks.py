#!/usr/bin/env python3

"""
This module demonstrates an asynchronous routine named task_wait_n.
It spawns task_wait_random n times with a specified max_delay.
It collects the delays in a list and sorts them in ascending order.
"""

import asyncio
from typing import List

# Assuming task_wait_random is imported or defined elsewhere
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters:
    1. n (int): The number of times to spawn task_wait_random.
    2. max_delay (int): The maximum delay in seconds for task_wait_random.

    Returns:
    1. list: A list[float] of delays in ascending order.
    """

    delays = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        delay = await task
        delays.append(delay)

    # Sort the delays in ascending order
    sorted_delays = sorted(delays)

    return sorted_delays
