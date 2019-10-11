import click

import terraincache
from rasterio.rio import options


@click.command("terraincache")
@click.option(
    "--out_file", "-o", default="terrain-tiles.tif", type=click.Path(resolve_path=True)
)
@click.option(
    "--bounds",
    callback=options.bounds_handler,
    required=True,
    help='Bounds: "left bottom right top" or "[left, bottom, right, top]".',
)
@click.option("--zoom", "-z", type=int, required=True, help="Web map zoom level")
@click.option("--path", envvar="TERRAINCACHE")
@click.option(
    "-r",
    "--res",
    type=float,
    default=25,
    help="Output dataset resolution in meters (square pixels)",
)
@click.option(
    "--dst-crs", default="EPSG:3005", help="Target coordinate reference system."
)
def cli(out_file, bounds, zoom, path, res, dst_crs):
    """Write terrain tiles to geotiff"""
    terraincache.merge(bounds, zoom, path, res=res, dst_crs=dst_crs, out_file=out_file)


if __name__ == "__main__":
    terraincache()
