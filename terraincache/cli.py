import click
import logging
import sys

import terraincache
from raserio.warp import transform_bounds
from rasterio.rio import options
from cligj import verbose_opt, quiet_opt


@click.command("terraincache")
@click.option(
    "--out_file",
    "--out-file",
    "-o",
    default="terrain-tiles.tif",
    type=click.Path(resolve_path=True),
)
@click.option(
    "--bounds",
    callback=options.bounds_handler,
    required=True,
    help='Bounds: "left bottom right top" or "[left, bottom, right, top]".',
)
@click.option("--zoom", "-z", type=int, required=True, help="Web map zoom level")
@click.option("--cache-path", "--cache_path", "-p", envvar="TERRAINCACHE")
@click.option(
    "-r",
    "--res",
    type=float,
    default=25,
    help="Output dataset resolution in meters (square pixels)",
)
@click.option(
    "--bounds-crs", "--bounds_crs", help="CRS of provided bounds", default="EPSG:4326"
)
@click.option(
    "--dst-crs",
    "--dst_crs",
    default="EPSG:3005",
    help="Target coordinate reference system.",
)
@verbose_opt
@quiet_opt
def cli(out_file, bounds, zoom, path, res, bounds_crs, dst_crs, verbose, quiet):
    """Write terrain tiles to geotiff"""
    verbosity = verbose - quiet
    log_level = max(10, 30 - 10 * verbosity)
    logging.basicConfig(stream=sys.stderr, level=log_level)
    if bounds_crs != "EPSG:4326":
        bounds = transform_bounds(bounds_crs, "EPSG:4326", *bounds)
    terraincache.merge(bounds, zoom, path, res=res, dst_crs=dst_crs, out_file=out_file)


if __name__ == "__main__":
    terraincache()
