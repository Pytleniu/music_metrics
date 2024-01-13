# ZPRP - Projekt zespół 16
### Authors: Michał Kopeć, Wiktor Pytlewski

# Music metrics

This repository hosts the source code for `music_metrics`, a Python package developed as part of the Advanced Programming in Python course at Warsaw University of Technology. The music-metrics package integrates various music metrics from libraries such as `muspy`, `pretty_midi` and `pypianoroll`, offering a consolidated toolkit for music analysis. The package is structured around different types of metrics:
- Harmonic metrics
- Pitch metrics
- Rhythm metrics


## Installation guide

Currently, the Music-Metrics package is not available on [PyPI](https://pypi.org/). To install, you need to clone the repository and perform a local installation using pip.

Clone the repository:
```commandline
git clone https://github.com/Pytleniu/music_metrics.git
cd music_metrics
```
Install the package:
```commandline
pip install scib
```
To use music-metrics in your Python project, simply import it:
```python
import music_metrics
```

## Contribution guide

Contributions to music_metrics are welcome! If you're interested in enhancing the library or fixing bugs, please follow the steps below to set up your development environment.

### Setting Up the Development Environment
Install the necessary dependencies:
```commandline
pip install -r requirements
```
### Running Tests
To ensure that everything is set up correctly and functioning as expected, you can run the tests using tox:
```commandline
tox
```
Your contributions will help improve the library and are greatly appreciated!