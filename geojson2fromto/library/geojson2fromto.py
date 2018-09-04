"""
Module for converting geojson to from-to json.
"""

import sys
from functools import reduce
import simplejson as json
import geopandas

def get_geometries(input_file_path):
    """
    Reads a GeoJSON input file and ouputs a geopandas.GeoSeries object
    with geometries.
    """

    data_frame = geopandas.read_file(input_file_path)

    return data_frame['geometry']

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

def convert(input_file_path):
    """
    Converts a GeoJSON file to a list with dictionaries containing from
    and to fields.
    """

    geometries = get_geometries(input_file_path)

    return reduce(
        (lambda fromtos, geometry: fromtos + get_fromtos(geometry)),
        geometries,
        []
    )

def main(argv=sys.argv): # pylint: disable=dangerous-default-value
    """
    Exposes the CLI of geojson2fromto
    """

    json.encoder.FLOAT_REPR = lambda x: format(x, '.15f')

    inputfile_path = str(argv[1])

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
