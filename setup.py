try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cdef

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
]

REQUIREMENTS = [
    'pytz',
]

setup(
    name='rrd-cdef',
    author='Tomasz Rybarczyk',
    author_email='paluho@gmail.com',
    version = cdef.__version__,
    url='http://github.com/paluh/rrd-cdef',
    description='Trivial DSL for RRD CDEFs.',
    py_modules=['cdef'],
    install_requires=REQUIREMENTS,
    test_suite='tests',
    zip_safe=False,
    classifiers=CLASSIFIERS,
)
