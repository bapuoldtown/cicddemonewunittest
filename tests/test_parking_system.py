import pytest
from app_codes.parking_system import ParkingSystem


@pytest.mark.component
def test_reserve_mid():
    sob = ParkingSystem("grand_i10", "mid")
    sob.reserve_mid()
    assert ParkingSystem.display() is not None


@pytest.mark.component
def test_reserve_large():
    sob = ParkingSystem("isuzu", "large")
    sob.reserve_large()
    assert ParkingSystem.display() is not None
