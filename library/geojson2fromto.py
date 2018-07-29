"""
Module for converting geojson to from-to json.
"""

from functools import reduce
import geopandas

def get_geometries(input_file_path):
    """
    Reads a GeoJSON input file and ouputs a geopandas.GeoSeries object
    with geometries.
    """

    data_frame = geopandas.read_file(input_file_path)

    return data_frame['geometry']

def get_fromtos(linestring_coords):
    """
    Converts a list of linestring coordinates to a list of 'from-to'
    dictionaries.
    """
    line_coordinates_list_froms = linestring_coords[:-1]
    line_coordinates_list_tos = linestring_coords[1:]

    i = 0
    fromtos = []

    for i, val in enumerate(line_coordinates_list_froms):
        fromto_dict = {}
        fromto_dict['from'] = val
        fromto_dict['to'] = line_coordinates_list_tos[i]

        fromtos.append(fromto_dict)

    return fromtos

def get_fromtos_multi(multi_linestring_coords):
    """
    Converts a list of lists containing linestring coordinates to a
    list of 'from-to' dictionaries.
    """
    return reduce(
        (lambda fromtos, linestring: fromtos + get_fromtos(linestring)),
        multi_linestring_coords,
        []
    )

def convert(input_file_path):
    """
    Converts a GeoJSON file to a list with dictionaries containing from
    and to fields.
    """

    geometries = get_geometries(input_file_path)

    multi_linestring = geometries[0]
    multi_linestring_coords = list(map(
        lambda linestring: list(linestring.coords),
        list(multi_linestring.geoms)
    ))

    return get_fromtos_multi(multi_linestring_coords)
