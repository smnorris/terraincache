import os
from pathlib import Path

import mercantile
from mercantile import Tile

import terraincache
from terraincache import tile_path


TEST_TILE = Tile(x=622, y=1364, z=12)
TEST_BOUNDS = (-125.271412, 51.370639, -125.254793, 51.376881)
TEST_ZOOM_1 = 12
TEST_ZOOM_2 = 14


def test_download_single_tile(tmpdir):
    terraincache.download(TEST_BOUNDS, TEST_ZOOM_1, str(tmpdir))
    assert Path(str(tmpdir)).joinpath("/".join(tile_path(TEST_TILE))).exists()


def test_download_bounds(tmpdir):
    tiles = mercantile.tiles(*TEST_BOUNDS, TEST_ZOOM_2)
    terraincache.download(TEST_BOUNDS, TEST_ZOOM_2, str(tmpdir))
    for tile in tiles:
        assert Path(str(tmpdir)).joinpath("/".join(tile_path(tile))).exists()


def test_download_bounds_zooms(tmpdir):
    tiles = mercantile.tiles(*TEST_BOUNDS, [TEST_ZOOM_1, TEST_ZOOM_2])
    terraincache.download(TEST_BOUNDS, [TEST_ZOOM_1, TEST_ZOOM_2], str(tmpdir))
    for tile in tiles:
        assert Path(str(tmpdir)).joinpath("/".join(tile_path(tile))).exists()


def test_merge(tmpdir):
    terraincache.merge(
        TEST_BOUNDS,
        TEST_ZOOM_2,
        cache=str(tmpdir),
        out_file=os.path.join(str(tmpdir), "test.tif"))
    assert (Path(str(tmpdir)) / "test.tif").exists
