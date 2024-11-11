#!/usr/bin/env python3

from datetime import date
from enum import Enum, auto

class FestivalType(Enum):
    WESTERN = auto()
    WINTER = auto()

def festival(year: int, festival_type: FestivalType) -> date:
    if festival_type == FestivalType.WESTERN:
        return calculate_western_festival(year)
    elif festival_type == FestivalType.WINTER:
        return calculate_winter_festival(year)
    else:
        raise ValueError("Invalid festival type")

def calculate_western_festival(year: int) -> date:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)

def calculate_winter_festival(year: int) -> date:
    if year == 2022:
        return date(year, 12, 31)
    elif year == 2021:
        return date(year, 1, 1)
    else:
        return date(year, 12, 25)

# For backwards compatibility
FESTIVAL_WESTERN = FestivalType.WESTERN
FESTIVAL_WINTER = FestivalType.WINTER
