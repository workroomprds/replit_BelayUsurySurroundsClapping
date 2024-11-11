#!/usr/bin/env python3
from typing import List, Union

def bucketise(items: List[Union[int, float]], bucket_size: int = 10) -> List[List[Union[int, float]]]:
    _validate_inputs(items, bucket_size)
    
    sorted_items = sorted(items)
    buckets = []
    
    for item in sorted_items:
        if not buckets or item - buckets[-1][0] >= bucket_size:
            buckets.append([item])
        else:
            buckets[-1].append(item)
    
    return buckets

def _validate_inputs(items: List[Union[int, float]], bucket_size: int) -> None:
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    if not isinstance(bucket_size, int) or bucket_size <= 0:
        raise ValueError("Bucket size must be a positive integer")
