import os
import sys

from setuptools import setup, find_packages

from pyexample import NAME, VERSION

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description='Python example application.',
    long_description=long_description,
    author='Minoru Osuka',
    author_email='minoru.osuka@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    url='https://github.com/mosuka/pyexample',
    packages=find_packages('.'),
    platforms='any',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'pyexample = pyexample.__main__:main'
        ]
    },
    test_suite='tests'
)
