#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
 async_comprehension four times in parallel using asyncio.gather.
"""


import asyncio
from typing import Generator
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    """
    This coroutine measures the time it will take to execute
    async_comprehension four times in parallel using asyncio.gath.
    """

    """
    start_time = time.time()

    total_tasks = [async_comprehension for i in range(4)]
    results = await asyncio.gather(*total_tasks)

    end_time = time.time()

    total_runtime = end_time - start_time

    return total_runtime
"""

    start_time = asyncio.get_event_loop().time()

    total_tasks = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*total_tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
