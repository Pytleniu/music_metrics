import muspy
import pypianoroll
from prettytable import PrettyTable

from utils import load_representations


def get_rythm_metrics(data: any):
    muspy_representation, midi_representation, pianoroll_representation = load_representations(
        data)

    empty_beat_rate = drum_in_pattern_rate = drum_pattern_consistency = groove_consistency = \
        empty_measure_rate = tempo_change_times = tempo = n_times_tempo_change = end_time = \
        tempos = probabilities = estimate_tempo = beats = beat_start = downbeats = n_beats = \
        onsets = n_notes = time_signatures = n_signatures = qualified_note_rate = None

    # muspy
    if muspy_representation:
        empty_beat_rate = muspy.empty_beat_rate(music=muspy_representation)
        drum_in_pattern_rate = muspy.drum_in_pattern_rate(
            music=muspy_representation, meter='duple')  # meter in ['duple', 'triple']
        drum_pattern_consistency = muspy.drum_pattern_consistency(
            music=muspy_representation)
        groove_consistency = muspy.groove_consistency(
            music=muspy_representation, measure_resolution=1)
        empty_measure_rate = muspy.empty_measure_rate(
            music=muspy_representation, measure_resolution=1)

    # pretty_midi
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
    # if pianoroll_representation:
    #     qualified_note_rate = pypianoroll.qualified_note_rate(pianoroll_representation)

    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'empty_beat_rate': '',
        'drum_in_pattern_rate': '',
        'drum_pattern_consistency': '',
        'groove_consistency': '',
        'empty_measure_rate': '',
        'tempo_changes': '',
        'n_times_tempo_change': '',
        'end_time': '',
        'estimate_tempi': '',
        'estimate_tempo': '',
        'beats': '',
        'beat_start': '',
        'downbeats': '',
        'n_beats': '',
        'onsets': '',
        'n_notes': '',
        'time_signatures': '',
        'n_signatures': '',
        'qualified_note_rate': '',
    }

    rythm_metrics = {
        'empty_beat_rate': empty_beat_rate,
        'drum_in_pattern_rate': drum_in_pattern_rate,
        'drum_pattern_consistency': drum_pattern_consistency,
        'groove_consistency': groove_consistency,
        'empty_measure_rate': empty_measure_rate,
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
        'qualified_note_rate': qualified_note_rate,
    }

    for metric, value in rythm_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return rythm_metrics, metrics_table
