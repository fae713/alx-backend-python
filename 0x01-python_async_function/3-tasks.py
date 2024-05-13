#!/usr/bin/env python3

"""
Write a synchronous function task_wait_random
that takes an integer max_delay and returns a asyncio.Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """
    paramaeters:
        1. max_delay = time it takes to return the wait_random

    return:
        1. asyncio.task
    """

    coroutine = wait_random(max_delay)

    task = asyncio.create_task(coroutine)

    return task
