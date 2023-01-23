from setuptools import setup
from __version__ import VERSION

setup(
    name="catg",
    version=VERSION,
    license="MIT",
    packages=["catg"],
    entry_points={"console_scripts": ["catg = catg.interface.command:cli"]},
)
