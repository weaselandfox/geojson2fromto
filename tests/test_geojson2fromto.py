# pylint: disable=redefined-outer-name

"""
Test for geojson2fromto.
"""

import os
import pytest
from geojson2fromto.library import geojson2fromto

@pytest.fixture()
def convert_parameters():
    """
    Fixture function.
    """
    test_input = os.path.abspath(os.path.join(__file__, os.pardir) + '/fixtures/roads.geojson')

    expected_output = [{
        'from': (5.29304565210666, 51.683623536234776),
        'to': (5.293036226696422, 51.67776112527045)
    }, {
        'from': (5.293036226696422, 51.67776112527045),
        'to': (5.29302863902825, 51.677771119362951)
    }, {
        'from': (5.29302863902825, 51.677771119362951),
        'to': (5.293018976918102, 51.677782224485654)
    }]

    return test_input, expected_output

@pytest.fixture()
def convert_multi_parameters():
    """
    Fixture function.
    """
    test_input = os.path.abspath(
        os.path.join(__file__, os.pardir) + '/fixtures/roads_multiline.geojson'
    )

    expected_output = [{
        'from': (5.29304565210666, 51.677748170157187),
        'to': (5.293036226696422, 51.67776112527045)
    }, {
        'from': (5.293036226696422, 51.67776112527045),
        'to': (5.29302863902825, 51.677771119362951)
    }, {
        'from': (5.29302863902825, 51.677771119362951),
        'to': (5.293018976918102, 51.677782224485654)
    }, {
        'from': (5.293018976918102, 51.677782224485654),
        'to': (5.293006100024401, 51.677792310480484)
    }, {
        'from': (5.293006100024401, 51.677792310480484),
        'to': (5.292990286295295, 51.677801836140205)
    }, {
        'from': (5.292990286295295, 51.677801836140205),
        'to': (5.292980854535434, 51.677806353823691)
    }]

    return test_input, expected_output

@pytest.fixture()
def convert_features_parameters():
    """
    Fixture function.
    """
    test_input = os.path.abspath(
        os.path.join(__file__, os.pardir) + '/fixtures/roads_multiline_features.geojson'
    )

    expected_output = [{
        'from': (5.29304565210666, 51.677748170157187),
        'to': (5.293036226696422, 51.67776112527045)
    }, {
        'from': (5.293036226696422, 51.67776112527045),
        'to': (5.29302863902825, 51.677771119362951)
    }, {
        'from': (5.29302863902825, 51.677771119362951),
        'to': (5.293018976918102, 51.677782224485654)
    }, {
        'from': (5.293018976918102, 51.677782224485654),
        'to': (5.293006100024401, 51.677792310480484)
    }, {
        'from': (5.293006100024401, 51.677792310480484),
        'to': (5.292990286295295, 51.677801836140205)
    }, {
        'from': (5.292990286295295, 51.677801836140205),
        'to': (5.292980854535434, 51.677806353823691)
    }, {
        'from': (5.293184004341166, 51.677927885896217),
        'to': (5.293170313261858, 51.677914957221006),
    }, {
        'from': (5.293170313261858, 51.677914957221006),
        'to': (5.293162434034709, 51.677908618118778),
    }, {
        'from': (5.293162434034709, 51.677908618118778),
        'to': (5.293145956592333, 51.677901166138092),
    }, {
        'from': (5.293131483208716, 51.677895977248333),
        'to': (5.293111071340474, 51.677889225908949),
    }, {
        'from': (5.293111071340474, 51.677889225908949),
        'to': (5.293098779778031, 51.67788533141325),
    }, {
        'from': (5.293098779778031, 51.67788533141325),
        'to': (5.293085286201258, 51.677881180490346)
    }]

    return test_input, expected_output

def test_convert(convert_parameters):
    """
    It should convert input geojson to 'from-to' json.
    """
    test_input = convert_parameters[0]
    expected_output = convert_parameters[1]
    assert geojson2fromto.convert(test_input) == expected_output

def test_convert_multi(convert_multi_parameters):
    """
    It should concatenate all linestrings in a multi linestring.
    """
    test_input = convert_multi_parameters[0]
    expected_output = convert_multi_parameters[1]
    assert geojson2fromto.convert(test_input) == expected_output

def test_convert_features(convert_features_parameters):
    """
    It should concatenate all features in a FeatureCollection.
    """
    test_input = convert_features_parameters[0]
    expected_output = convert_features_parameters[1]
    assert geojson2fromto.convert(test_input) == expected_output
