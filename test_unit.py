import pytest
from tax import Trip, Taximeter

# ==========================
# Test 1: Trip.to_dict()
# ==========================
def test_trip_to_dict():
    trip = Trip("2025-12-15T12:00:00", stopped_time=10, moving_time=20, total_fare=5.0)
    expected = {
        "start_time": "2025-12-15T12:00:00",
        "stopped_time": 10,
        "moving_time": 20,
        "total_fare": 5.0
    }
    assert trip.to_dict() == expected

# ==========================
# Test 2: Iniciar viaje
# ==========================
def test_start_trip():
    taximeter = Taximeter()
    # Evitar usar la DB real
    taximeter.db = None
    taximeter.start_trip()
    assert taximeter.trip_active
    assert taximeter.state == "stopped"
    assert taximeter.start_time is not None

# ==========================
# Test 3: Calcular tarifa
# ==========================
def test_calculate_fare():
    taximeter = Taximeter()
    taximeter.stopped_time = 10
    taximeter.moving_time = 20
    fare = taximeter.calculate_fare()
    assert fare == pytest.approx(10*0.02 + 20*0.05)
