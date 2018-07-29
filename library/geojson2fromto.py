import geopandas

def convert(inputFilePath):
  dataFrame = geopandas.read_file(inputFilePath)

  line = dataFrame['geometry'][0]
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

  return a
