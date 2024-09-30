#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages, setup

__location__ = os.path.dirname(__file__)


def get_install_requirements(path):
    with open(os.path.join(__location__, path)) as fh:
        content = fh.read()
    return [req for req in content.splitlines() if req != ""]


def read(fname):
    with open(os.path.join(__location__, fname)) as fh:
        content = fh.read()
    return content


def prepare_data_files(dct):
    import glob

    return [
        (k, [f for p in v.split(",") for f in filter(os.path.isfile, glob.glob(p))])
        for k, v in dct.items()
    ]


# In github actions the base directory is "build" and in the local setup the base directory is 'dist' where symlinks are located.
BASE_DIR = "cpp/build"


#DATA_FILES = {
#    "./pylyric/lib/": f"./cpp/build//*.so",
#}
#data_files = prepare_data_files(DATA_FILES)

_package_data = ['lib/*.so']

# Assemble everything and call setup(...)
def setup_package():
    install_reqs = get_install_requirements("./requirements.txt")

    setup(
        name="mylyric",
        version='1.0.0',
        long_description="Lyric Package",
        author="Lyric Technologies",
        install_requires=install_reqs,
        #tests_require=["pytest-cov", "pytest"],
        classifiers=[
            "Development Status :: Alpha",
            "Programming Language :: Python 3.10",
        ],
        packages=find_packages(exclude=["tests", "tests.*"]),
        package_data={'mylyric':  _package_data},
        # Use the below to copy additional stuff under data folder. E.g sql files etc
        #data_files=data_files,
        zip_safe=False,
    )  # do not zip egg file after setup.py install


if __name__ == "__main__":
    setup_package()
