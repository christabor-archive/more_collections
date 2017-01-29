"""Extended collection data structures for python."""

import os

from setuptools import setup

SRCDIR = '.'
folder = os.path.abspath(os.path.dirname(__file__))
test_requirements = [
    'pytest==3.0',
    'pytest-cov==2.4',
]
requirements = []

setup(
    name='more_collections',
    version='0.0.1',
    description='Extended collection data structures for python.',
    long_description=__doc__,
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    url='https://github.com/christabor/more_collections',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require=test_requirements,
    install_requires=requirements,
    package_dir={'more_collections': 'more_collections'},
    packages=['more_collections'],
    zip_safe=False,
    include_package_data=True,
)
