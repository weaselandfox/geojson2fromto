"""
Main entry file for the geojson2fromto module.
"""

import sys
import json
from library import geojson2fromto

INPUTFILE_PATH = str(sys.argv[1])

try:
    OUTPUTFILE_PATH = str(sys.argv[2])
except IndexError:
    OUTPUTFILE_PATH = None

FROMTO = geojson2fromto.convert(INPUTFILE_PATH)

if OUTPUTFILE_PATH is not None:
    with open(OUTPUTFILE_PATH, 'w') as outfile:
        json.dump(FROMTO, outfile)
else:
    sys.stdout.write(json.dumps(FROMTO))
