from src.romanNumerals import romanToArabic, arabicToRoman
import pytest

def test_romanToArabic():
	assert romanToArabic("I") == 1

def test_arabicToRoman():
	assert arabicToRoman(1) == "I"