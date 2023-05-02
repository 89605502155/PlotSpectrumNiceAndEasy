from io import open
from setuptools import setup


version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PlotSpectrumNiceAndEasy',
    version=version,

    author='Andrey Ferubko',
    author_email='ferubko1999@yandex.ru',

    description=(
        'It is a Python library for build a very nice spectrum and theory lines of elements. But you can plot an other plots. It is an extension of the matplotlib library'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/89605502155/PlotSpectrumNiceAndEasy',
    download_url='https://github.com/89605502155/PlotSpectrumNiceAndEasy/archive/v{}.zip'.format(
        version
    ),
    # download_url='https://github.com/89605502155/MetrPlot/archive/main.zip',

    license='GNU General Public License v3.0',

    packages=['PlotSpectrumNiceAndEasy'],
    install_requires=['numpy','MetrPlot'],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)