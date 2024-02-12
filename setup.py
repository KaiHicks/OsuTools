from pathlib import Path
from setuptools import find_packages, setup

module_path = Path(__file__).parent / Path("src")
setup(
    name="osutools",
    version="1.0",
    packages=["osutools"],
    where="src",
    package_dir={"": "src"},
)
