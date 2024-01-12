import muspy
import pypianoroll
from prettytable import PrettyTable

from .utils import load_representations

def get_rythm_metrics(data: any):
    
    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    empty_beat_rate = drum_in_pattern_rate_duple = drum_in_pattern_rate_triple = drum_pattern_consistency = groove_consistency = \
    tempo_change_times = tempo = n_times_tempo_change = end_time = \
    tempos = probabilities = estimate_tempo = beats = beat_start = downbeats = n_beats = \
    onsets = n_notes = time_signatures = n_signatures = qualified_note_rate = None

    # muspy
    if muspy_representation:
        empty_beat_rate = muspy.empty_beat_rate(music=muspy_representation)
        drum_in_pattern_rate_duple = muspy.drum_in_pattern_rate(music=muspy_representation, meter='duple') # meter in ['duple', 'triple']
        drum_in_pattern_rate_triple = muspy.drum_in_pattern_rate(music=muspy_representation, meter='duple') # meter in ['duple', 'triple']
        drum_pattern_consistency = muspy.drum_pattern_consistency(music=muspy_representation)
        groove_consistency = muspy.groove_consistency(music=muspy_representation, measure_resolution=4)

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
    # if pianoroll_representation.any():
    #     qualified_note_rate = pypianoroll.qualified_note_rate(pianoroll_representation, threshold=1)

    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'empty_beat_rate': 'The proportion of empty bars in a song to the total number of bars.',
        'drum_in_pattern_rate_duple': 'The ratio of percussion notes that fit a specific rhythmic pattern (duple) to the total number of percussion notes in the song. Only percussion tracks are taken into account.',
        'drum_in_pattern_rate_triple': 'The ratio of percussion notes that fit a specific rhythmic pattern (triple) to the total number of percussion notes in the song. Only percussion tracks are taken into account.',
        'drum_pattern_consistency': 'The largest value of the drum_in_pattern metric. Only percussion tracks are taken into account.',
        'groove_consistency': 'Returns a floating-point value that determines the regularity and repeatability of the rhythm. The higher the value, the more regular the rhythm is. The value returned by metric can be in the range [0, 1]. The metric is only usable for songs that have a fixed meter and a minimum of two bars.',
        'tempo_changes': 'A tuple with two elements, the first is an array with the time locations at which the rate changes, the second is an array with the rate values at changed at given times.',
        'n_times_tempo_change': 'A value that tells how many times the tempo changes during a song.',
        'end_time': 'Time of the song',
        'estimate_tempi': 'A tuple with two element, the first is an array of potential tempos for a song in the bpm unit, the second is an array with probability of how well the tempo matches the song.',
        'estimate_tempo': 'The tempo of the song with the highest probability of matching the song',
        'beats': 'An array of note time locations depending on the song\'s meter, e.g. for the 6/8 meter it returns the third and sixth eighth notes, while for the 4/4 meter it returns each quarter note.',
        'beat_start': 'The time location of the beginning of the song',
        'downbeats': 'An array of first beats in bars expressed in seconds',
        'n_beats': 'Number of bars with downbeat',
        'onsets': 'An array with all notes in song',
        'n_notes': 'Number of all notes in song',
        'time_signatures': 'An array of musical meter changes in a song, along with timestamps of their occurrences.',
        'n_signatures': 'Number of musical meter changes',
        # 'qualified_note_rate': 'The metric returns the proportion of notes considered qualitative i.e. those that last longer than the declared threshold to all notes available in the piece.',
    }

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

    for metric, value in rythm_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return rythm_metrics, metrics_table