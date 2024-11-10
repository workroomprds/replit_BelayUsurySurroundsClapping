#!/usr/bin/env python3

from datetime import date, timedelta

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

    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    
    easter_date = date(year, month, day)

    if method == EASTER_JULIAN:
        # For Julian Easter, we need to subtract 13 days from the Gregorian date
        return easter_date - timedelta(days=13)
    elif method == EASTER_ORTHODOX:
        # For Orthodox Easter, we need to add the difference between Gregorian and Julian calendars
        century = year // 100
        difference = 13 if century >= 20 else 12
        return easter_date + timedelta(days=difference)
    else:  # EASTER_WESTERN
        return easter_date
