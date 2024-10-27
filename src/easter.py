#!/usr/bin/env python3

from datetime import date

EASTER_WESTERN = 'western'
EASTER_ORTHODOX = 'orthodox'
EASTER_JULIAN = 'julian'

def easter(year, method=EASTER_WESTERN):
    """
    Calculate Easter date for given year using specified method.
    
    :param year: Year to calculate Easter for
    :param method: Method to use (western, orthodox, or julian)
    :return: Date object representing Easter date
    """
    if method not in [EASTER_WESTERN, EASTER_ORTHODOX, EASTER_JULIAN]:
        raise ValueError("Invalid method. Use 'western', 'orthodox', or 'julian'.")

    # Meeus/Jones/Butcher algorithm
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

    if method == EASTER_JULIAN:
        # Julian calendar
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return date(year, month, day)
    elif method == EASTER_ORTHODOX:
        # Orthodox Easter (Julian Easter + 13 days)
        julian_easter = easter(year, EASTER_JULIAN)
        return julian_easter.replace(day=julian_easter.day + 13)
    else:
        # Western (Gregorian) Easter
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return date(year, month, day)
