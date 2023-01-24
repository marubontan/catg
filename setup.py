from setuptools import setup
from __version__ import VERSION

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="catg",
    version=VERSION,
    license="MIT",
    packages=["catg"],
    install_requires=required,
    entry_points={"console_scripts": ["catg = catg.interface.command:cli"]},
)
