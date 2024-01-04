import muspy
import pypianoroll
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

from utils import load_representations

def plot_pitch_class_histogram(histogram):
    plt.bar(np.arange(12), histogram)
    plt.xticks(np.arange(12), ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'])
    plt.xlabel('Note')
    plt.ylabel('Proportion')

def compute_best_scale(muspy_representation):
    roots = [i for i in range(12)]
    modes = ['major', 'minor']

    results = defaultdict(int)

    for mode in modes:
        results[mode] = {}
        for root in roots:
            pitch_in_scale_rate = muspy.pitch_in_scale_rate(muspy_representation, root=root, mode=mode)
            results[mode][root] = pitch_in_scale_rate

    major_scale = max(results['major'].items(), key=lambda r: r[1])
    minor_scale = max(results['minor'].items(), key=lambda r: r[1])

    return major_scale, minor_scale

def get_pitch_metrics(data: any):
    
    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    pitch_range = n_pitches_used = n_pitch_classes_used = pitch_entropy = \
    pitch_class_entropy = pitch_class_histogram = chroma = pitch_range_tuple = None

    # muspy
    if muspy_representation:
        pitch_range = muspy.pitch_range(music=muspy_representation)
        n_pitches_used = muspy.n_pitches_used(music=muspy_representation)
        n_pitch_classes_used = muspy.n_pitch_classes_used(music=muspy_representation)
        major_scale, minor_scale = compute_best_scale(muspy_representation)
        pitch_entropy = muspy.pitch_entropy(music=muspy_representation)
        pitch_class_entropy = muspy.pitch_class_entropy(music=muspy_representation)

    # pretty_midi
    if midi_representation:
        pitch_class_histogram = midi_representation.get_pitch_class_histogram()
        chroma = midi_representation.get_chroma()

    # pypianoroll
    # if pianoroll_representation:
    #     print(type(pianoroll_representation))    
    #     pitch_range_tuple = pypianoroll.pitch_range_tuple(pianoroll_representation)

    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'pitch_range': "Range of pitches used",
        'pitch_range_tuple': "Tuple of pitches range",
        'n_pitches_used': "Number of different pitches used",
        'n_pitch_classes_used': "Number of different pitch classes used",
        'major_scale': "",
        'minor_scale': "",
        'pitch_entropy': "Entropy of pitches (measure of randomness)",
        'pitch_class_entropy': "Entropy of pitch classes (measure of randomness)",
        'pitch_class_histogram': 'pitch_class_histogram',
        'chroma': 'chroma',
    }

    pitch_metrics = {
        'pitch_range': pitch_range,
        'pitch_range_tuple': pitch_range_tuple,
        'n_pitches_used': n_pitches_used,
        'n_pitch_classes_used': n_pitch_classes_used,
        'major_scale': major_scale,
        'minor_scale': minor_scale,
        'pitch_entropy': pitch_entropy,
        'pitch_class_entropy': pitch_class_entropy,
        'pitch_class_histogram': pitch_class_histogram,
        'chroma': chroma,
    }

    for metric, value in pitch_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return pitch_metrics, metrics_table