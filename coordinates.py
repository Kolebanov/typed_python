from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using PC GPS"""
    return Coordinates(latitude=0.0, longitude=0.0)