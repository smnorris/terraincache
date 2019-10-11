import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Parse the version
with open("terraincache/__init__.py", "r") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

requires = ["click", "rasterio", "mercantile"]

test_requirements = ["pytest"]

setup(
    name="terraincache",
    version=version,
    url="https://github.com/smnorris/terraincache",
    description=u"Basic tool for downloading and merging mapzen terrain tile geotiffs from AWS",
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="terrain-tiles mapzen aws terrain dem s3 geotiff",
    author=u"Simon Norris",
    author_email="snorris@hillcrestgeo.ca",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={"test": test_requirements},
    entry_points="""
      [console_scripts]
      terraincache=terraincache.cli:cli
      """,
)
