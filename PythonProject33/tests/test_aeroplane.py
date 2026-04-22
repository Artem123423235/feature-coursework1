import pytest
from src.models.aeroplane import Aeroplane


def test_aeroplane_creation():
    plane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
    assert plane.callsign == "UAL1621"
    assert plane.country_of_origin == "United States"
    assert plane.velocity == 268.79
    assert plane.altitude == 10203.18


def test_aeroplane_invalid_velocity():
    with pytest.raises(TypeError):
        Aeroplane("UAL1621", "United States", "fast", 10203.18)


def test_aeroplane_comparison_by_altitude():
    p1 = Aeroplane("A", "X", 100, 1000)
    p2 = Aeroplane("B", "X", 200, 2000)
    assert p1 < p2
    

def test_aeroplane_comparison_by_velocity():
    p1 = Aeroplane("A", "X", 100, 1000)
    p2 = Aeroplane("B", "X", 200, 2000)
    assert p2 > p1
