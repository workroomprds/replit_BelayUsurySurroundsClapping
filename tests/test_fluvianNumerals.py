from src.fluvianNumerals import fluvianToArabic, arabicToFluvian
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
		(11, "AB")
])
def test_fluvianToArabic(arabic, fluvian):
	assert fluvianToArabic(fluvian) == arabic


def test_arabicToFluvian():
	assert arabicToFluvian(1) == "A"
