from src.festival import festival
from src.festival import FESTIVAL_WESTERN, FESTIVAL_WINTER

from datetime import date
import pytest

# List of festivals between 1990 and 2050
western_festival_dates = [
    date(1990, 4, 15),
    date(1991, 3, 31),
    date(1992, 4, 19),
    date(1993, 4, 11),
    date(1994, 4, 3),
    date(1995, 4, 16),
    date(1996, 4, 7),
    date(1997, 3, 30),
    date(1998, 4, 12),
    date(1999, 4, 4),
    date(2000, 4, 23),
    date(2001, 4, 15),
    date(2002, 3, 31),
    date(2003, 4, 20),
    date(2004, 4, 11),
    date(2005, 3, 27),
    date(2006, 4, 16),
    date(2007, 4, 8),
    date(2008, 3, 23),
    date(2009, 4, 12),
    date(2010, 4, 4),
    date(2011, 4, 24),
    date(2012, 4, 8),
    date(2013, 3, 31),
    date(2014, 4, 20),
    date(2015, 4, 5),
    date(2016, 3, 27),
    date(2017, 4, 16),
    date(2018, 4, 1),
    date(2019, 4, 21),
    date(2020, 4, 12),
    date(2021, 4, 4),
    date(2022, 4, 17),
    date(2023, 4, 9),
    date(2024, 3, 31),
    date(2025, 4, 20),
    date(2026, 4, 5),
    date(2027, 3, 28),
    date(2028, 4, 16),
    date(2029, 4, 1),
    date(2030, 4, 21),
    date(2031, 4, 13),
    date(2032, 3, 28),
    date(2033, 4, 17),
    date(2034, 4, 9),
    date(2035, 3, 25),
    date(2036, 4, 13),
    date(2037, 4, 5),
    date(2038, 4, 25),
    date(2039, 4, 10),
    date(2040, 4, 1),
    date(2041, 4, 21),
    date(2042, 4, 6),
    date(2043, 3, 29),
    date(2044, 4, 17),
    date(2045, 4, 9),
    date(2046, 3, 25),
    date(2047, 4, 14),
    date(2048, 4, 5),
    date(2049, 4, 18),
    date(2050, 4, 10)
]

winter_festival_dates =  [
  date(2024, 12, 25),
  date(2023, 12, 26),
  date(2022, 12, 31),
  date(2021, 1, 1),
  date(2020, 12, 25)
]

@pytest.mark.parametrize("festival_date", western_festival_dates)
def test_festival_western(festival_date):
	assert festival_date == festival(festival_date.year, FESTIVAL_WESTERN)

@pytest.mark.parametrize("festival_date", winter_festival_dates)
def test_festival_winter(festival_date):
  assert festival_date == festival(festival_date.year, FESTIVAL_WINTER)

def test_festival_bad_method():
	with pytest.raises(ValueError):
		festival(1975, 4)
