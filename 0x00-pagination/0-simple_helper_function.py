#!/usr/bin/env python3
"""
0-simple_helper_function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple (start index, end index)
    """
    start_index = page_size * (page - 1)
    end_index = page_size + start_index
    return start_index, end_index
