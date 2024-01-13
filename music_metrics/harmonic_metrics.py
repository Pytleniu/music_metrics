import muspy
# import pypianoroll
from prettytable import PrettyTable

from .utils import load_representations


def get_harmonic_metrics(data: any):
    """
    Calculate various harmonic metrics for a given musical data.

    This function analyzes the harmonic aspects of a musical piece, utilizing
    different representations and libraries to compute metrics like polyphony,
    polyphony rate, pitch class transition matrix, and tonal distance.

    Parameters
    ----------
    data : any
        The input data for which harmonic metrics are to be calculated.
        The format of this data is flexible and handled by :func:`utils.load_representations`.

    Returns
    -------
    tuple
        A tuple containing two elements:
            1. Dictionary of calculated harmonic metrics.
            2. :class:`PrettyTable` object summarizing these metrics along with their descriptions.

    Notes
    -----
    The function currently uses **muspy** for metric calculations.
    Future implementations may include metrics from other libraries such as **pretty_midi** and **pypianoroll**.
    """
    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    # Initializing metrics
    polyphony = polyphony_rate = pitch_class_transition_matrix = tonal_distance = None

    # Calculations using muspy
    polyphony = muspy.polyphony(music=muspy_representation)
    polyphony_rate = muspy.polyphony_rate(music=muspy_representation)

    # Placeholder for pitch_class_transition_matrix calculation (pretty_midi)
    # pitch_class_transition_matrix = midi_representation.get_pitch_class_transition_matrix()

    # Placeholder for tonal_distance calculation (pypianoroll)
    # tonal_distance = pypianoroll.tonal_distance(
    #     pianoroll_1=pianoroll_representation,
    #     pianoroll_2=pianoroll_representation,
    #     resolution=1
    # )

    # Preparing a table for metrics display
    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'polyphony': 'The average number of sounds played at one time. Percussion tracks are not taken into '
                     'account.',
        'polyphony_rate': 'The ratio of temporal moments in which more than one sound is played to the duration '
                          'of the entire piece. Provides information about the frequency of polyphony in a given '
                          'piece.',
        'pitch_class_transition_matrix': 'A transition matrix representing how often each sound class (e.g., C, C#, '
                                         'D, etc.) transitions to another sound class in a song. Used for harmonic '
                                         'analysis of a piece',
        'tonal_distance': 'The tonal distance between the two specified music rolls. The returned value is a '
                          'floating point number. Tonal distance is used to describe the degree of harmonic and '
                          'tonal similarity between two pieces of music.',
    }

    # Collecting calculated metrics
    harmonic_metrics = {
        'polyphony': polyphony,
        'polyphony_rate': polyphony_rate,
        'pitch_class_transition_matrix': pitch_class_transition_matrix,
        'tonal_distance': tonal_distance,
    }

    # Populating the table with metrics and descriptions
    for metric, value in harmonic_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return harmonic_metrics, metrics_table
