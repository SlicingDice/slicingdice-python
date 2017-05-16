import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pyslicer",
    version="1.0.0",
    author="SlicingDice LLC",
    author_email="help@slicingdice.com",
    description="Official Python client for SlicingDice, Data Warehouse and Analytics Database as a Service.",
    install_requires=["requests", "six", "ujson"],
    license="BSD",
    keywords="slicingdice slicing dice data analysis analytics database",
    packages=[
        'pyslicer',
        'pyslicer.core',
        'pyslicer.utils',
    ],
    package_dir={'pyslicer': 'pyslicer'},
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
