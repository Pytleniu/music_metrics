import muspy
# import pypianoroll - can be enabled if needed
from prettytable import PrettyTable

from .utils import load_representations


def get_rythm_metrics(data: any):
    """
    Calculate various rhythm-related metrics for a given musical data.

    This function analyzes the rhythm aspects of a musical piece, utilizing
    different representations and libraries to compute metrics like empty beat rate,
    drum pattern consistency, groove consistency, tempo changes, and more.

    Parameters
    ----------
    data : any
        The input data for which rhythm metrics are to be calculated.
        The format of this data is flexible and handled by :func:`utils.load_representations`.

    Returns
    -------
    tuple
        A tuple containing two elements:
            1. Dictionary of calculated rhythm metrics.
            2. :class:`PrettyTable` object summarizing these metrics along with their descriptions.

    Notes
    -----
    The module currently uses **muspy** and **pretty_midi** for metric calculations.
    Future implementations may include metrics from other libraries such as **pypianoroll**.
    """

    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    # Initializing metrics
    empty_beat_rate = drum_in_pattern_rate_duple = drum_in_pattern_rate_triple = drum_pattern_consistency \
        = groove_consistency = tempo_change_times = tempo = n_times_tempo_change = end_time = \
        tempos = probabilities = estimate_tempo = beats = beat_start = downbeats = n_beats = \
        onsets = n_notes = time_signatures = n_signatures = None

    # Calculate metrics using muspy
    if muspy_representation:
        empty_beat_rate = muspy.empty_beat_rate(music=muspy_representation)
        drum_in_pattern_rate_duple = muspy.drum_in_pattern_rate(
            music=muspy_representation, meter='duple')  # meter in ['duple', 'triple']
        drum_in_pattern_rate_triple = muspy.drum_in_pattern_rate(
            music=muspy_representation, meter='duple')  # meter in ['duple', 'triple']
        drum_pattern_consistency = muspy.drum_pattern_consistency(music=muspy_representation)
        groove_consistency = muspy.groove_consistency(music=muspy_representation, measure_resolution=4)

    # Calculate metrics using pretty_midi
    if midi_representation:
        tempo_change_times, tempo = midi_representation.get_tempo_changes()
        n_times_tempo_change = len(tempo_change_times)
        end_time = midi_representation.get_end_time()
        tempos, probabilities = midi_representation.estimate_tempi()
        estimate_tempo = midi_representation.estimate_tempo()
        beats = midi_representation.get_beats(start_time=0.0)
        beat_start = midi_representation.estimate_beat_start()
        downbeats = midi_representation.get_downbeats()
        n_beats = len(downbeats)
        onsets = midi_representation.get_onsets()
        n_notes = len(onsets)
        time_signatures = midi_representation.time_signature_changes
        n_signatures = len(time_signatures)

    # pypianoroll
    # if pianoroll_representation.any():
    #     qualified_note_rate = pypianoroll.qualified_note_rate(pianoroll_representation, threshold=1)

    # Prepare a table for displaying metrics
    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'empty_beat_rate': 'The proportion of empty bars in a song to the total number of bars.',
        'drum_in_pattern_rate_duple': 'The ratio of percussion notes fitting a specific rhythmic pattern '
                                      '(duple) to the total number of percussion notes. Only percussion '
                                      'tracks are considered.',
        'drum_in_pattern_rate_triple': 'The ratio of percussion notes fitting a specific rhythmic pattern '
                                       '(triple) to the total number of percussion notes. Only percussion '
                                       'tracks are considered.',
        'drum_pattern_consistency': 'The largest value of the drum_in_pattern metric. Only percussion tracks '
                                    'are considered.',
        'groove_consistency': 'Returns a floating-point value for the regularity and repeatability of the '
                              'rhythm. Higher values indicate more regular rhythms. Applicable to songs with '
                              'a fixed meter and a minimum of two bars.',
        'tempo_changes': 'A tuple: first element is an array of time locations for tempo changes; second is '
                         'an array of tempo values at those times.',
        'n_times_tempo_change': 'Number of times the tempo changes during a song.',
        'end_time': 'Duration of the song.',
        'estimate_tempi': 'A tuple: first element is an array of potential tempos (bpm); second is an array '
                          'of probabilities for each tempo.',
        'estimate_tempo': 'The most likely tempo of the song.',
        'beats': 'An array of note time locations based on the song\'s meter (e.g., third and sixth '
                 'eighth notes for 6/8 meter, each quarter note for 4/4 meter).',
        'beat_start': 'Time location of the beginning of the song.',
        'downbeats': 'An array of the first beats in bars, expressed in seconds.',
        'n_beats': 'Number of bars with downbeat.',
        'onsets': 'An array of all note onsets in the song.',
        'n_notes': 'Total number of notes in the song.',
        'time_signatures': 'An array of musical meter changes in the song, with timestamps.',
        'n_signatures': 'Number of musical meter changes in the song.',
        # 'qualified_note_rate': 'The proportion of notes longer than a certain threshold to all notes in the piece.'
    }
    # Collecting calculated metrics
    rythm_metrics = {
        'empty_beat_rate': empty_beat_rate,
        'drum_in_pattern_rate_duple': drum_in_pattern_rate_duple,
        'drum_in_pattern_rate_triple': drum_in_pattern_rate_triple,
        'drum_pattern_consistency': drum_pattern_consistency,
        'groove_consistency': groove_consistency,
        'tempo_changes': (tempo_change_times, tempo),
        'n_times_tempo_change': n_times_tempo_change,
        'end_time': end_time,
        'estimate_tempi': (tempos, probabilities),
        'estimate_tempo': estimate_tempo,
        'beats': beats,
        'beat_start': beat_start,
        'downbeats': downbeats,
        'n_beats': n_beats,
        'onsets': onsets,
        'n_notes': n_notes,
        'time_signatures': time_signatures,
        'n_signatures': n_signatures,
        # 'qualified_note_rate': qualified_note_rate,
    }
    # Populating the table with metrics and descriptions
    for metric, value in rythm_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return rythm_metrics, metrics_table
