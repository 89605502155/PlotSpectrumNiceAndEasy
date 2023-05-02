# PlotSpectrumNiceAndEasy

![PyPI](https://img.shields.io/pypi/v/PlotSpectrumNiceAndEasy?color=orange) ![Python 3.8, 3.9, 3.10, 3.11, 3.12](https://img.shields.io/pypi/pyversions/PlotSpectrumNiceAndEasy?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/89605502155/PlotSpectrumNiceAndEasy?color=blueviolet) ![License](https://img.shields.io/pypi/l/PlotSpectrumNiceAndEasy?color=blueviolet) ![Forks](https://img.shields.io/github/forks/89605502155/PlotSpectrumNiceAndEasy?style=social)

**PlotSpectrumNiceAndEasy** - this module is a Python library for the N-PLS1 regression with L2-regularization.


## Installation

Install the current version with [PyPI](https://pypi.org/project/):

```bash
pip install PlotSpectrumNiceAndEasy
```
Ubuntu:
```
pip3 install PlotSpectrumNiceAndEasy
```
Or from Github:
```bash
pip install https://github.com/89605502155/PlotSpectrumNiceAndEasy/main.zip
```

## Usage

You can plot a very nice spectrum and theory lines of elements. But you can plot an other plots like this. It is an extension of the matplotlib library.

```python
from PlotSpectrumNiceAndEasy import PlotSpectrumNiceAndEasy

a=[1,2,3,4,5,6,7]
b=[0.02,2,-5,0,9,6,1]
model=PlotSpectrumNiceAndEasy(name_plot="Spectrum",save_name="test_plot",y_name="Intensity",x_name="lambda, nm")
result=model.main(a,b,save=True,Pb=[1,1,0,5,"red"],Hf=[2,2,1,3,"orange"])
```

## Example

You can see an example of the plot in test_plot.png and test_plot.svg files on the repository of this library.

