try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

REQUIREMENTS = [
    'pytz',
]

setup(
    name='rrd-cdef',
    author='Tomasz Rybarczyk',
    author_email='paluho@gmail.com',
    version = '2013.08.1',
    url='http://github.com/paluh/rrd-cdef',
    description='Trivial DSL for RRD CDEFs.',
    py_modules=['cdef'],
    install_requires=REQUIREMENTS,
    test_suite='tests',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
