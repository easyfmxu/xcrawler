from setuptools import setup
from setuptools import find_packages

from xcrawler import __version__, __author__, __license__
setup(
    name = "xcrawler",
    version = __version__,
    author = __author__,
    license = __license__,
    packages = find_packages(),
)
