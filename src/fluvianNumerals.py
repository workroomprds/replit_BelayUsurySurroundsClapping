#!/usr/bin/env python3

def fluvianToArabic(fluvian):
    fluvian_map = {
        'A': 1,
        'B': 12,
        'C': 3,
        'D': 6,
    }
    return fluvian_map.get(fluvian, 0)

def arabicToFluvian(arabic):
    arabic_map = {
        1: 'A',
        12: 'B',
        3: 'C',
        6: 'D',
    }
    return arabic_map.get(arabic, "")
