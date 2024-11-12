from src.fluvianNumerals import fluvianToArabic, arabicToFluvian
import pytest

def test_fluvianToArabic():
	assert fluvianToArabic("A") == 1

def test_arabicToFluvian():
	assert arabicToFluvian(1) == "A"