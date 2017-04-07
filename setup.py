# Cashier setup.py script
#
# It doesn't depend on setuptools, but if setuptools is available it'll use
# some of its features, like package dependencies.

import os
from cashier import meta_data
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
base_dir = os.path.dirname(__file__)


setup_args = {
    'name': 'cashier',
    'version': meta_data.get("version"),
    'url': meta_data.get("version"),
    'description': meta_data.get("description"),
    'author': meta_data.get("author"),
    'author_email': 'atmb4u@gmail.com',
    'license': meta_data.get("license"),
    'include_package_data': True,
    'py_modules': ['cashier/__init__'],
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
}

packages = [
    "cashier",
]

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(**setup_args)
