import geocoder
import math
from typing import Union


def decimal_to_osm(lat_deg: float, lon_deg: float, zoom: int) -> tuple:
    """ converts decimal coordinates to internal OSM coordinates
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""

    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = (lon_deg + 180.0) / 360.0 * n
    ytile = (1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n
    return xtile, ytile


def osm_to_decimal(tile_x: Union[int, float], tile_y: Union[int, float], zoom: int) -> tuple:
    """ converts internal OSM coordinates to decimal coordinates 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""

    n = 2.0 ** zoom
    lon_deg = tile_x / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * tile_y / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lon_deg


def convert_coordinates_to_address(deg_x: float, deg_y: float) -> geocoder.osm_reverse.OsmReverse:
    """ returns address object with the following attributes:
        street, housenumber, postal, city, state, country, latlng
        Geocoder docs: https://geocoder.readthedocs.io/api.html#reverse-geocoding 

        Author: Tom Schimansky | https://github.com/TomSchimansky"""

    result = geocoder.osm([deg_x, deg_y], method="reverse")
    return result


def convert_coordinates_to_city(deg_x: float, deg_y: float) -> str:
    """ returns city name 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    return geocoder.osm([deg_x, deg_y], method="reverse").city


def convert_coordinates_to_country(deg_x: float, deg_y: float) -> str:
    """ returns country name 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    return geocoder.osm([deg_x, deg_y], method="reverse").country


def convert_address_to_coordinates(address_string: str) -> tuple:
    """ returns address object for given coords or None if no address found 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""

    result = geocoder.osm(address_string)

    if result.ok:
        return tuple(result.latlng)
    else:
        return None
