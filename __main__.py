from library import geojson2fromto
import sys
import json

inputFilePath = str(sys.argv[1])

try:
    outputFilePath = str(sys.argv[2])
except IndexError:
    outputFilePath = None

a = geojson2fromto.convert(inputFilePath);
if outputFilePath != None:
    with open(outputFilePath, 'w') as outfile:
        json.dump(a, outfile)
else:
    sys.stdout.write(json.dumps(a))
