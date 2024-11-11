#!/usr/bin/env python3
from typing import List, Union

def bucketise(items: List[Union[int, float]], bucket_size: int = 10) -> List[List[Union[int, float]]]:
    _validate_inputs(items, bucket_size)
    
    sorted_items = sorted(items)
    buckets = []
    current_bucket = []
    
    for item in sorted_items:
        if _should_add_to_current_bucket(current_bucket, item, bucket_size):
            current_bucket.append(item)
        else:
            buckets.append(current_bucket)
            current_bucket = [item]
    
    if current_bucket:
        buckets.append(current_bucket)
    
    return buckets

def _validate_inputs(items: List[Union[int, float]], bucket_size: int) -> None:
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    if not isinstance(bucket_size, int) or bucket_size <= 0:
        raise ValueError("Bucket size must be a positive integer")

def _should_add_to_current_bucket(current_bucket: List[Union[int, float]], 
                                  item: Union[int, float], 
                                  bucket_size: int) -> bool:
    return len(current_bucket) == 0 or item - current_bucket[0] < bucket_size
