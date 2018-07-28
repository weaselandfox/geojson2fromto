import sys
import geopandas

inputFilePath = str(sys.argv[1])
dataFrameFroms = geopandas.read_file(inputFilePath)
dataFrameTos = geopandas.read_file(inputFilePath)

print(inputFilePath)

line = dataFrameFroms['geometry'][0]
lineCoords = list(list(line.geoms)[0].coords)

print(lineCoords)
