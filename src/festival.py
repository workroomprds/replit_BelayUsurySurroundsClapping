#!/usr/bin/env python3

from datetime import date, timedelta

FESTIVAL_WESTERN = 'western'
FESTIVAL_WINTER = 'winter'

def festival(year, method):
    if method == FESTIVAL_WESTERN:
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
    elif method == FESTIVAL_WINTER:
        return date(year, 12, 25)
    else:
        raise ValueError("Invalid method")
