from typing import NamedTuple
import geocoder
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current coordinates using PC GPS"""
    g = geocoder.ip('me')
    g_class_name = type(g).__name__
    # print(type(g_class_name))
    if (g is None) or g_class_name != 'IpinfoQuery':
        raise CantGetCoordinates
   
    latitude = g.latlng[0]
    longitude = g.latlng[1]
    # print(g.latlng)
    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    print(get_coordinates())