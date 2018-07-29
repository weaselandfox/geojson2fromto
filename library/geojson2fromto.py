"""
Module for converting geojson to from-to json.
"""

import geopandas

def get_geometries(input_file_path):
    """
    Reads a GeoJSON input file and ouputs a geopandas.GeoSeries object
    with geometries.
    """

    data_frame = geopandas.read_file(input_file_path)

    return data_frame['geometry']

def get_fromto(linestring_coords):
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

def convert(input_file_path):
    """
    Converts a GeoJSON file to a list with dictionaries containing from
    and to fields.
    """

    geometries = get_geometries(input_file_path)

    multi_linestring = geometries[0]
    linestring_coords = list(list(multi_linestring.geoms)[0].coords)

    return get_fromto(linestring_coords)
