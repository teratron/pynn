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
        name='netix',
        version=os.getenv('PACKAGE_VERSION', '0.0.dev0'),
        description='Neural network library.',
        author='Oleg Alexandrov',
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'pynn*'
        ]),
        install_requires=[
            *read_pipenv_dependencies('Pipfile.lock')
        ]
    )

# setup(
#     name='home.news',
#     version='0.1',
#     description='News for Django',
#     author='Elias',
#     namespace_packages=['home'],                                                                      # line 8
#     packages=find_packages(),
#     platforms='any',
#     zip_safe=False,
#     include_package_data=True,
#     dependency_links=['git+ssh://git@git.home.com/app-admintools@v0.1#egg=admintools-0.1'],           # line 13
#     install_requires=['admintools==0.1'],                                                             # line 14
#     classifiers=[
#         'Development Status :: 5 - Production/Stable',
#         'Environment :: Web Environment',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: BSD License',
#         'Operating System :: OS Independent',
#         'Programming Language :: Python',
#         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
#         'Framework :: Django',
#     ],
# )
