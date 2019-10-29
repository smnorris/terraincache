import os
from pathlib import Path

import mercantile
from mercantile import Tile

from terraincache import TerrainTiles


TEST_TILE = Tile(x=622, y=1364, z=12)
TEST_BOUNDS = (-125.271412, 51.370639, -125.254793, 51.376881)
TEST_ZOOM_1 = 12
TEST_ZOOM_2 = 14


def tile_path(tile):
    return "/".join([str(tile.z), str(tile.x), str(tile.y) + ".tif"])


def test_download_single_tile(tmpdir):
    tt = TerrainTiles(TEST_BOUNDS, TEST_ZOOM_1, cache_dir=str(tmpdir))
    tt.download_tile(TEST_TILE)
    assert Path(str(tmpdir)).joinpath(tile_path(TEST_TILE)).exists()


def test_download_bounds(tmpdir):
    tt = TerrainTiles(TEST_BOUNDS, TEST_ZOOM_2, cache_dir=str(tmpdir))
    for tile in mercantile.tiles(*TEST_BOUNDS, TEST_ZOOM_2):
        assert Path(str(tmpdir)).joinpath(tile_path(tile)).exists()


def test_merge(tmpdir):
    tt = TerrainTiles(TEST_BOUNDS, TEST_ZOOM_2, cache_dir=str(tmpdir))
    tt.merge(out_file=os.path.join(str(tmpdir), "merged.tif"))
    assert (Path(str(tmpdir)) / "merged.tif").exists


def test_warp(tmpdir):
    tt = TerrainTiles(
        TEST_BOUNDS,
        TEST_ZOOM_2,
        cache_dir=str(tmpdir),
        dst_crs="EPSG:3005",
        resolution=50,
    )
    tt.merge()
    tt.warp(out_file=os.path.join(str(tmpdir), "warped.tif"))
    assert (Path(str(tmpdir)) / "warped.tif").exists


def test_load(tmpdir):
    tt = TerrainTiles(
        TEST_BOUNDS,
        TEST_ZOOM_2,
        cache_dir=str(tmpdir),
        dst_crs="EPSG:3005",
        resolution=50,
    )
    array = tt.load()
    assert array.shape == (14, 23)
