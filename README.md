# ZPRP - Projekt zespół 16
### Authors: Michał Kopeć, Wiktor Pytlewski

# Music metrics

This repository is home to the music_metrics Python package, developed as a part of the Advanced Programming in Python course at Warsaw University of Technology. The `music-metrics` package integrates various music analysis metrics from libraries such as `muspy`, `pretty_midi`, and `pypianoroll`, creating a unified platform for music evaluation. The package categorizes metrics into distinct types: different types of metrics:
- Harmonic metrics
- Pitch metrics
- Rhythm metrics


## Installation guide

Currently, the `Music-Metrics` package is not available on [PyPI](https://pypi.org/). To install, you need to clone the repository and perform a local installation using pip.

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
Verify correct setup and functionality by executing tests with `tox`:
```commandline
tox
```
Your contributions will help improve the library and are greatly appreciated!

## Summary of current work

Our ongoing efforts have focused on utilizing individual files of prevalent musical dataset types for evaluation processes. The supported file formats include:
- `.mid` and `.midi`
- `.xml` and `.musicxml`
- `.npz`

Additionally, our library supports different types of data for evaluation, including:
- `pypianoroll.Multitrack`
- `pypianoroll.Track`
- `pretty_midi.PrettyMIDI`
- `music21.stream.Stream`
- `music21.stream.Opus`
- `music21.stream.Part`
- `music21.stream.Score`

### Future Development Opportunities

- **Advanced Metrics for Music Assessment**:
  - Incorporate advanced metrics that use neural network models for calculations.
  - Metrics to consider:
    - `Inception Score`
    - `Frechet Audio Distance`
    - `Kernel Inception Distance`
  - Aim: Enhance the depth and accuracy of music evaluation.

- **Automated Pipeline for Dataset Analysis**:
  - Develop an automated pipeline utilizing our library.
  - Purpose: To streamline the evaluation process.
  - Benefit: Facilitate efficient dataset comparisons and assessments.

- **Performance Testing on Large Datasets**:
  - Include performance testing with extensive datasets.
  - Goal: Assess the library’s efficiency and scalability.
  - Focus: Determine how well the library handles large-scale music data.

- **Enhanced Data Export Capabilities**:
  - Implement functionality to save metric results in various file formats.
  - Objective: Enhance user flexibility in data handling and representation.
  - Advantage: Provide users with more options for data storage and analysis.
