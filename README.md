# geojson2fromto

> Python module that converts GeoJSON to DECK.GL's LineLayer 'from-to'


## Install

```
$ pip install geojson2fromto
```

## Usage

```
geojson2fromto data.geojson [from-to-data.json]
```


## Dev Install


```
$ git@github.com:weaselandfox/geojson2fromto.git
$ cd geojson2fromto
$ pipenv install

```


## Dev Usage


```
$ pipenv shell
$ pipenv run python . input.geojson output.json
```

There are multiple command-line options available:

```
$ geojson2fromto --help

  geojson2fromto takes a GeoJSON file and outputs JSON with 'from-to' data to
  STDOUT or writes to an optional output-file

  Usage:
    geojson2fromto [options] input-file [ouput-file]

  Options:
    --help          # Print the generator's options and usage


## License

MIT © [Weasel & Fox](https://www.weaselandfox.com)
