geojson2fromto
==============

   Python module that converts LineStrings and MultiLineStrings of a
   GeoJSON FeatureCollection to DECK.GL’s LineLayer ‘from-to’

Requirements
------------

-  Python 3 - 3.6. Python 3.7 doesn’t work due to `pyproj’s lack of
   support for Python
   3.7 <https://github.com/jswhit/pyproj/issues/136>`__ which is a
   dependency of `geopandas <https://github.com/geopandas/geopandas>`__
   which has `it’s own related
   issue <https://github.com/geopandas/geopandas/issues/793>`__ to this

Install
-------

::

   $ pip install geojson2fromto

Usage
-----

::

   $ geojson2fromto data.geojson [from-to-data.json]

--------------

**Note:** To use the resulting JSON with Deck.GL’s LineLayer the
``coordinateSystem`` prop of the LineLayer has to be set to
``COORDINATE_SYSTEM.LNGLAT_EXPERIMENTAL``

Dev Install
-----------

::

   $ git@github.com:weaselandfox/geojson2fromto.git
   $ cd geojson2fromto
   $ pipenv install

Dev Usage
---------

::

   $ pipenv shell
   $ python . input.geojson output.json

Tests
~~~~~

Make sure you have activated a virtualenv (run ``$ pipenv shell``)

::

   $ pytest

License
-------

MIT © `Weasel & Fox <https://www.weaselandfox.com>`__
