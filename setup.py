# Cashier setup.py script
#
# It doesn't depend on setuptools, but if setuptools is available it'll use
# some of its features, like package dependencies.

import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
base_dir = os.path.dirname(__file__)


setup_args = {
    'name': 'cashier',
    'version': '1.0',
    'url': 'http://atmb4u.github.io/cashier',
    'description': 'Caching for python functions',
    'author': 'Anoop Thomas Mathew',
    'author_email': 'atmb4u@gmail.com',
    'license': 'BSD',
    'include_package_data': True,
    'py_modules': ['cashier/__init__'],
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
}

packages=[
    "cashier",
]

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(**setup_args)
