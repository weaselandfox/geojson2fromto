import sys
import json
import geopandas

inputFilePath = str(sys.argv[1])
outputFilePath = str(sys.argv[2])
dataFrameFroms = geopandas.read_file(inputFilePath)
dataFrameTos = geopandas.read_file(inputFilePath)

line = dataFrameFroms['geometry'][0]
lineCoordinatesList = list(list(line.geoms)[0].coords)

lineCoordinatesListA = lineCoordinatesList[:-1]
lineCoordinatesListB = lineCoordinatesList[1:]

i = 0
d = {}
a = []

for i in range(len(lineCoordinatesListA)):
    d['from'] = lineCoordinatesListA[i]
    d['to'] = lineCoordinatesListB[i]

    a.append(d)

with open(outputFilePath, 'w') as outfile:
    json.dump(a, outfile)
