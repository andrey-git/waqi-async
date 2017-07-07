"""A setuptools based setup module."""

from setuptools import setup, find_packages

setup(
    name='waqiasync',
    version='1.0.0',
    description='asyncio-friendly python API for aqicn.org',
    long_description='asyncio-friendly python API for World Air Quality Index (http://aqicn.org). Requires Python 3.4+',
    url='https://github.com/andrey-git/waqi-async',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='waqi',
    install_requires=['aiohttp', 'async_timeout'],
    zip_safe=True,
    author = 'andrey-git',
    author_email = 'andrey-git@github.com',
    packages=find_packages()
)