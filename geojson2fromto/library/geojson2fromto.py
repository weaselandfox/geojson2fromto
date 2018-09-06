"""
Module for converting geojson to from-to json.
"""

import sys
import math
from functools import reduce
import simplejson as json
import geopandas

def get_data_frame(input_file_path):
    """
    Reads a GeoJSON input file and returns a geopandas DataFrame object.
    """

    return geopandas.read_file(input_file_path)

def get_geometries(data_frame):
    """
    Returns a geopandas GeoSeries object with geometries from a DataFrame.
    """

    return data_frame['geometry']

def get_properties(data_frame):
    """
    Returns a list of dictionaries containing the properties of
    the features.
    """

    return data_frame.drop(columns=['geometry']).to_dict('records')


def get_fromtos_line(linestring_coords):
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

def get_fromtos_multi(multi_linestring):
    """
    Converts a GeoSeries with MuiltiLineStrings to a list of 'from-to'
    dictionaries.
    """
    multi_linestring_coords = list(map(
        lambda linestring: list(linestring.coords),
        list(multi_linestring.geoms)
    ))

    return reduce(
        (lambda fromtos, linestring: fromtos + get_fromtos_line(linestring)),
        multi_linestring_coords,
        []
    )


def get_fromtos(geometry):
    """
    Converts a LineString or MultiLineString geometry to a list of
    'from-to' dictionaries.
    """
    if geometry is None:
        return []

    geom_type = geometry.geom_type

    if geom_type == 'LineString':
        return get_fromtos_line(geometry.coords)

    if geom_type == 'MultiLineString':
        return get_fromtos_multi(geometry)
    return []

def merge_fromto_with_properties(fromto, properties):
    """
    Merges a dictionary with from to elements with an array of dictionaries
    with properties.
    """
    index, coords = fromto
    property_index = min(math.floor(index / 2), len(properties) - 1)

    if bool(properties[property_index]):
        coords['properties'] = properties[property_index]

    return coords

def convert(input_file_path):
    """
    Converts a GeoJSON file to a list with dictionaries containing from
    and to fields.
    """

    data_frame = get_data_frame(input_file_path)
    geometries = get_geometries(data_frame)
    properties = get_properties(data_frame)

    fromtos = reduce(
        (lambda fromtos, geometry: fromtos + get_fromtos(geometry)),
        geometries,
        []
    )

    fromtos_properties = map(
        lambda fromto: merge_fromto_with_properties(fromto, properties),
        enumerate(fromtos),
    )

    return list(fromtos_properties)

def main(argv=sys.argv): # pylint: disable=dangerous-default-value
    """
    Exposes the CLI of geojson2fromto
    """

    json.encoder.FLOAT_REPR = lambda x: format(x, '.15f')


    try:
        inputfile_path = str(argv[1])
    except IndexError:
        sys.stdout.write("Please provide a path to the input geojson file as the first argument")
        return False

    try:
        outputfile_path = str(argv[2])
    except IndexError:
        outputfile_path = None

    fromto = convert(inputfile_path)

    if outputfile_path is not None:
        with open(outputfile_path, 'w') as outfile:
            json.dump(fromto, outfile)
    else:
        sys.stdout.write(json.dumps(fromto))

    return True
