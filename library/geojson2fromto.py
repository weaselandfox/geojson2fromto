"""
Module for converting geojson to from-to json.
"""

import geopandas

def convert(input_file_path):
    """
    Converts a GeoJSON file to a list with dictionaries containing from and to fields.
    """
    data_frame = geopandas.read_file(input_file_path)

    line = data_frame['geometry'][0]
    line_coordinates_list = list(list(line.geoms)[0].coords)

    line_coordinates_list_a = line_coordinates_list[:-1]
    line_coordinates_list_b = line_coordinates_list[1:]

    i = 0
    fromtos = []

    for i, val in enumerate(line_coordinates_list_a):
        fromto_dict = {}
        fromto_dict['from'] = val
        fromto_dict['to'] = line_coordinates_list_b[i]

        fromtos.append(fromto_dict)

    return fromtos
