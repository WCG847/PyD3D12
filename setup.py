from setuptools import setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True  # Force platform-specific wheel
    def is_pure(self):
        return False

setup(distclass=BinaryDistribution)
