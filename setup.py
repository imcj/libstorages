# -*- coding: utf-8 -
#
# copy from gunicorn setup


import os
from setuptools import setup, find_packages, Command
import sys

CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content']

# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

# read dev requirements
fname = os.path.join(os.path.dirname(__file__), 'requirements.txt')k
with open(fname) as f:
    tests_require = list(map(lambda l: l.strip(), f.readlines()))


class NoseTest ( Command ):
    user_options = []

    def __init__ ( self, *args, **kwargs ):
        # super ( NoseTest, self ).__init__ ( *args, **kwargs )
        Command.__init__ ( self, *args, **kwargs )

    def initialize_options ( self ):
        self.p = True

    def finalize_options ( self ):
        pass

    def run ( self ):
        import sys, subprocess
        errno = subprocess.call ( [ "nosetests", "-s" ] )
        raise SystemExit ( errno )

setup(
    name = 'cloudstore',
    version = '0.0.2',

    description = 'Cloud Store API',
    long_description = long_description,
    author = 'CJ',
    author_email = 'weicongju@gmail.com',
    license = 'MIT',
    url = 'http://bukaopu.us',

    classifiers = CLASSIFIERS,
    zip_safe = False,
    packages = find_packages(exclude=['tests']),
    include_package_data = True,

    tests_require = tests_require,
    cmdclass = { 'test' : NoseTest },

    entry_points=""
)
