import muspy
# import pypianoroll - Currently unused, can be enabled if needed
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

from .utils import load_representations

# Dictionary mapping pitch class numbers to their names
pitch_class = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F',
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}


def plot_pitch_class_histogram(histogram):
    """
    Plot a histogram of pitch class distribution.

    This function visualizes the distribution of pitch classes in a given musical piece
    as a bar chart.

    Parameters
    ----------
    histogram : array-like
        An array representing the frequency of each pitch class.
    """
    plt.bar(np.arange(12), histogram)
    plt.xticks(np.arange(12), ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'])
    plt.xlabel('Note')
    plt.ylabel('Proportion')
    plt.show()


def plot_chromagram(chromagram):
    """
    Plot the chromagram of a musical piece.

    This function visualizes the intensity of different pitch classes over time in a musical piece.

    Parameters
    ----------
    chromagram : array-like
        A 2D array representing the intensity of pitch classes over time.
    """
    plt.figure(figsize=(12, 8))
    plt.imshow(chromagram, aspect='auto', origin='lower', cmap='viridis')
    plt.colorbar(label='Intensity')
    plt.xlabel('Time (in 1/fs seconds)')
    plt.ylabel('Pitch Class (C, C#, D, ..., B)')
    plt.title('Chromagram')
    plt.show()


def compute_best_scale(muspy_representation):
    """
    Compute the most likely major and minor scales for a musical piece.

    This function calculates the likelihood of each major and minor scale for the given musical piece.

    Parameters
    ----------
    muspy_representation : muspy.Music
        A muspy music object representing a musical piece.

    Returns
    -------
    tuple
        A tuple containing two elements:
            1. The most probable major scale and its likelihood.
            2. The most probable minor scale and its likelihood.
    """
    # Calculating the most probable major and minor scales
    roots = [i for i in range(12)]
    modes = ['major', 'minor']

    results = defaultdict(int)

    # Iterate over modes and root notes to compute scale likelihood
    for mode in modes:
        results[mode] = {}
        for root in roots:
            pitch_in_scale_rate = muspy.pitch_in_scale_rate(muspy_representation, root=root, mode=mode)
            results[mode][root] = pitch_in_scale_rate

    # Determine the most probable scale
    major_scale = max(results['major'].items(), key=lambda r: r[1])
    minor_scale = max(results['minor'].items(), key=lambda r: r[1])

    return major_scale, minor_scale


def get_pitch_metrics(data: any):
    """
    Calculate various pitch-related metrics for a given musical data.

    This function analyzes the pitch aspects of a musical piece, utilizing
    different representations and libraries to compute metrics like pitch range,
    pitch entropy, pitch class entropy, and chroma.

    Parameters
    ----------
    data : any
        The input data for which pitch metrics are to be calculated.
        The format of this data is flexible and handled by :func:`utils.load_representations`.

    Returns
    -------
    tuple
        A tuple containing two elements:
            1. Dictionary of calculated pitch metrics.
            2. :class:`PrettyTable` object summarizing these metrics along with their descriptions.

    Notes
    -----
    The function currently uses **muspy** and **pretty_midi** for metric calculations.
    Future implementations may include metrics from other libraries such as **pypianoroll**.
    """
    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    # Initializing metrics
    pitch_range = n_pitches_used = n_pitch_classes_used = pitch_entropy = \
        pitch_class_entropy = pitch_class_histogram = chroma = None

    # Compute metrics using muspy
    if muspy_representation:
        pitch_range = muspy.pitch_range(music=muspy_representation)
        n_pitches_used = muspy.n_pitches_used(music=muspy_representation)
        n_pitch_classes_used = muspy.n_pitch_classes_used(music=muspy_representation)
        major_scale, minor_scale = compute_best_scale(muspy_representation)
        pitch_entropy = muspy.pitch_entropy(music=muspy_representation)
        pitch_class_entropy = muspy.pitch_class_entropy(music=muspy_representation)

    # Compute metrics using pretty_midi
    if midi_representation:
        pitch_class_histogram = midi_representation.get_pitch_class_histogram()
        chroma = midi_representation.get_chroma()

    # pypianoroll
    # if pianoroll_representation.size > 0:
        # pitch_range_tuple = pypianoroll.pitch_range_tuple(pianoroll_representation)

    # Processing major and minor scales for table display
    major_class_scale = (pitch_class[major_scale[0]], major_scale[1])
    minor_class_scale = (pitch_class[minor_scale[0]], minor_scale[1])

    # Initialize PrettyTable for metrics display
    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'pitch_range': "the difference between the maximum pitch value and the minimum "
        "pitch value",
        'n_pitches_used': "Number of different pitches used",
        'n_pitch_classes_used': "Number of different pitch classes used",
        'major_scale': "major_scale[0] - most probably major scale, major_scale[1] - "
                       "probability of that scale",
        'minor_scale': "minor_scale[0] - most probably minor scale, minor_scale[1] - "
                       "probability of that scale",
        'pitch_entropy': "Entropy of pitches (measure of randomness). The greater the "
                         "entropy value, the greater the pitch variation",
        'pitch_class_entropy': "Entropy of pitch classes (measure of randomness). The "
                               "greater the entropy value, the greater the pitch classes "
                               "variation",
        'pitch_class_histogram': 'A histogram of the proportions of each sound class to all '
                                 'sounds occurring in the piece. Visualization possible with '
                                 'the plot_chromagram function',
        'chroma': 'Chromogram - flattened for all instruments occurring in the song at a '
                  'given moment in time. Allows visualization and analysis of pitch '
                  'distribution over time. Visualization possible with the '
                  'plot_pitch_class_histogram function ',
    }
    # Collecting calculated metrics
    pitch_metrics = {
        'pitch_range': pitch_range,
        'n_pitches_used': n_pitches_used,
        'n_pitch_classes_used': n_pitch_classes_used,
        'major_scale': major_class_scale,
        'minor_scale': minor_class_scale,
        'pitch_entropy': pitch_entropy,
        'pitch_class_entropy': pitch_class_entropy,
        'pitch_class_histogram': pitch_class_histogram,
        'chroma': chroma,
    }
    # Populating the table with metrics and descriptions
    for metric, value in pitch_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return pitch_metrics, metrics_table
