#!/usr/bin/env python3
from typing import List, Union

def bucketise(items: List[Union[int, float]], bucket_size: int = 10) -> List[List[Union[int, float]]]:
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    if not isinstance(bucket_size, int) or bucket_size <= 0:
        raise ValueError("Bucket size must be a positive integer")
    
    sorted_items = sorted(items)
    buckets = []
    current_bucket = []
    
    for item in sorted_items:
        if len(current_bucket) == 0 or item - current_bucket[0] < bucket_size:
            current_bucket.append(item)
        else:
            buckets.append(current_bucket)
            current_bucket = [item]
    
    if current_bucket:
        buckets.append(current_bucket)
    
    return buckets
