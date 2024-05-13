#!/usr/bin/ env python3

"""
Create a measure_time function with integers n and max_delay
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""

import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> List[float]:
    """
    parameters:
        1. n (int) = the number of time to spawn wait_n.
        2. max_delay (int) = the time interval between wait_n.

    return:
        1. List[float] = the average time per delay for wait_n.
    """

    total_time = 0

    start_time = time.time()

    for i in range(n):
        asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
