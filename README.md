# terraincache

A basic Python script for downloading and accessing [Mapzen Terrain Tiles](https://registry.opendata.aws/terrain-tiles/) geotiffs from AWS.

## Installation

    git clone https://github.com/smnorris/terraincache
    cd terraincache
    pip install .

Set the `TERRAINCACHE` environment variable to save typing:

    export TERRAINCACHE=/users/snorris/Data/terrain-tiles

## Usage

### Python module

    from terraincache import TerrainTiles

    # initialize with zoom and bounds of interest,
    # specifiying crs and resolution of output grid
    tt = TerrainTiles(-125.271412, 51.370639, -125.254793, 51.376881, 11, dest_crs="EPSG:3005", resolution=50)

    # load to array
    array = tt.load()

    # dump to file
    tt.save(outfile="terrrain-tiles.tif")


### CLI

    $ terraincache --help
    Usage: terraincache [OPTIONS]

      Write terrain tiles to geotiff

    Options:
      -o, --out_file PATH
      --bounds TEXT        Bounds: "left bottom right top" or "[left, bottom,
                           right, top]".  [required]
      -z, --zoom INTEGER   Web map zoom level  [required]
      --path TEXT
      -r, --res FLOAT      Output dataset resolution in meters (square pixels)
      --dst-crs TEXT       Target coordinate reference system.
      --help               Show this message and exit.

Download Mt Waddington summit to a BC Albers geotiff, resampled to 25m:

    terraincache \
      --bounds "-125.271412, 51.370639, -125.254793, 51.376881" \
      --zoom 11 \
      --res 25 \
      terrain-tiles.tif


## Data sources

See the [data sources reference document](https://github.com/tilezen/joerd/blob/master/docs/data-sources.md)

## Credits

- [terrain-tiles](https://registry.opendata.aws/terrain-tiles)
- [Mapzen provided script](https://github.com/tilezen/joerd/blob/master/docs/examples/collect.py)
- [planetutils](https://github.com/interline-io/planetutils)
