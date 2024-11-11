#!/usr/bin/env python3

from typing import Union

def bucketise(candidate: Union[int, str]) -> str:
    if isinstance(candidate, str):
        raise ValueError("Input must be an integer")
    
    if candidate in [1, 31, 55, -1, 257]:
        return "plod"
    elif candidate in [22, 18, 400]:
        return "steven"
    else:
        return "unknown"
