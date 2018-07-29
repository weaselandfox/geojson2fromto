from library import geojson2fromto
import os
import pytest

@pytest.fixture()
def generate_convert_parameters(request):
  testInput = os.path.abspath(os.path.join(__file__, os.pardir) + '/fixtures/roads.geojson');

  expectedOutput = [{
    'from': [ 5.29304565210666, 51.677748170157187 ],
    'to': [ 5.293036226696422, 51.67776112527045 ]
  }, {
    'from': [ 5.293036226696422, 51.67776112527045 ],
    'to': [ 5.29302863902825, 51.677771119362951 ]
  }, {
    'from': [ 5.29302863902825, 51.677771119362951 ],
    'to': [ 5.293018976918102, 51.677782224485654 ]
  }]

  return testInput, expectedOutput

def test_convert(generate_convert_parameters):
    testInput = generate_convert_parameters[0]
    expectedOutput = generate_convert_parameters[1]
    assert geojson2fromto.convert(testInput) == expectedOutput
