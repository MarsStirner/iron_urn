# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'viruzzz-kun'
__version__ = '0.1'


if __name__ == '__main__':
    setup(
        name="iron-urn",
        version=__version__,
        description="URN Resolvers Service",
        long_description='',
        author=__author__,
        author_email="viruzzz.soft@gmail.com",
        license='ISC',
        url="https://stash.bars-open.ru/scm/medvtr/iron_urn",
        packages=["iron_urn"],
        zip_safe=False,
        install_requires=[
            'Flask',
            'flask-cache',
            'requests',
            'PyYaml',
            'simplejson',
            'hitsl.utils',
        ],
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: No Input/Output (Daemon)",
            "Programming Language :: Python",
            "Framework :: Flask",
            "Intended Audience :: Developers',"
        ])
