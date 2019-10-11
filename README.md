# terraincache

A basic Python script for downloading and accessing [Mapzen Terrain Tiles](https://registry.opendata.aws/terrain-tiles/) geotiffs from AWS.

## Installation

    pip install terraincache

## Setup

Set the `TERRAINCACHE` environment variable to save typing:

    export $TERRAINCACHE=/users/snorris/Data/terrain-tiles

## Python module

The python module downloads and dumps terrain tiles:

    import terraincache

    # download a bounds to cache
    bounds = (-125.271412, 51.370639, -125.254793, 51.376881)
    terraincache.download(bounds, 14, "/path/to/cache/folder")

    # dump tiles to BC Albers geotiff
    terraincache.merge(
        bounds,
        12,
        "/path/to/cache/folder",
        out_file="terrain-tiles.tif",
        dst_crs="EPSG:3005",
        res=30
    )

## CLI

### Usage

    $ terraincache --help
    Usage: terraincache [OPTIONS] OUT_FILE

      Write terrain tiles to geotiff

    Options:
      --bounds TEXT       Bounds: "left bottom right top" or "[left, bottom,
                          right, top]".  [required]
      -z, --zoom INTEGER  Web map zoom level  [required]
      --path TEXT
      -r, --res FLOAT     Output dataset resolution in meters (square pixels)
      --dst-crs TEXT      Target coordinate reference system.
      --help              Show this message and exit.

### Example

    terraincache \
      --bounds "(-125.271412, 51.370639, -125.254793, 51.376881" \
      --zoom 11 \
      --res 25 \
      terrain-tiles.tif


## Data sources and more

https://github.com/tilezen/joerd/blob/master/docs/data-sources.md

## Credits

https://registry.opendata.aws/terrain-tiles/
https://github.com/tilezen/joerd/blob/master/docs/examples/collect.py
https://github.com/interline-io/planetutils