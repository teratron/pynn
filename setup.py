"""setup.py script for packaging the project."""

import json
import os

from setuptools import setup, find_packages


def read_pipenv_dependencies(filename):
    """Get default dependencies from Pipfile.lock."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as lockfile:
        lock_json = json.load(lockfile)
        return [dependency for dependency in lock_json.get('default')]


if __name__ == '__main__':
    setup(
        name='pynn',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'pynn*'
        ]),
        description='Neural network library.',
        install_requires=[
            *read_pipenv_dependencies('Pipfile.lock'),
        ]
    )
