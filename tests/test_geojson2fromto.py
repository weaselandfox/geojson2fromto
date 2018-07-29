# pylint: disable=redefined-outer-name

"""
Test for geojson2fromto.
"""

import os
import pytest
from library import geojson2fromto

@pytest.fixture()
def generate_convert_parameters():
    """Fixture function to generate fixtures for the convert test"""
    test_input = os.path.abspath(os.path.join(__file__, os.pardir) + '/fixtures/roads.geojson')

    expected_output = [{
        'from': (5.29304565210666, 51.677748170157187),
        'to': (5.293036226696422, 51.67776112527045)
    }, {
        'from': (5.293036226696422, 51.67776112527045),
        'to': (5.29302863902825, 51.677771119362951)
    }, {
        'from': (5.29302863902825, 51.677771119362951),
        'to': (5.293018976918102, 51.677782224485654)
    }]

    return test_input, expected_output

def test_convert(generate_convert_parameters):
    """It should convert input geojson to 'from-to' json"""
    test_input = generate_convert_parameters[0]
    expected_output = generate_convert_parameters[1]
    assert geojson2fromto.convert(test_input) == expected_output
