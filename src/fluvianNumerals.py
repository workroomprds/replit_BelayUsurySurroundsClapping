#!/usr/bin/env python3

def fluvianToArabic(fluvian):
    fluvian_map = {
        'A': 1,
        'B': 12,
        'C': 3,
        'D': 6,
        'H': 72,
        'P': 144,
    }
    total = 0
    i = 0
    while i < len(fluvian):
        if i < len(fluvian) - 2 and fluvian[i:i+3] == 'AAD':
            total += 4
            i += 3
        elif i < len(fluvian) - 1 and fluvian[i:i+2] == 'AD':
            total += 5
            i += 2
        elif i < len(fluvian) - 1 and fluvian[i:i+2] == 'AA':
            total += 2
            i += 2
        else:
            current_value = fluvian_map.get(fluvian[i], 0)
            if i < len(fluvian) - 1:
                next_value = fluvian_map.get(fluvian[i+1], 0)
                if current_value < next_value:
                    total += next_value - current_value
                    i += 2
                    continue
            total += current_value
            i += 1
    return total

def arabicToFluvian(arabic):
    arabic_values = [(144, 'P'), (72, 'H'), (12, 'B'), (6, 'D'), (5, 'AD'), (4, 'AAD'), (3, 'C'), (2, 'AA'), (1, 'A')]
    result = ""
    for value, char in arabic_values:
        while arabic >= value:
            result += char
            arabic -= value
    return result

import pytest

@pytest.mark.parametrize("arabic, fluvian", [
    (1, "A"),
    (6, "D"),
    (12, "B"),
    (72, "H"),
    (144, "P"),
    (2, "AA"),
    (3, "AAA"),
    (4, "AAD"),
    (5, "AD"),
    (11, "AB"),
    (13, "BA"),
    (70, "AAH"),
    (71, "AH"),
    (73, "HA")
])
def test_fluvianToArabic(arabic, fluvian):
    assert fluvianToArabic(fluvian) == arabic

def test_arabicToFluvian():
    assert arabicToFluvian(1) == "A"
