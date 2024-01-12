import pytest
from music_metrics import get_pitch_metrics
from music_metrics import get_rythm_metrics
from music_metrics import get_harmonic_metrics

import pretty_midi
import pypianoroll

import os
from pathlib import Path


@pytest.fixture
def test_dir():
    test_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    return test_dir


@pytest.fixture
def midi_file_path(test_dir):
    # midi_file_path = 'datasets/tests_fur-elise.mid'
    midi_file_path = test_dir / '..' / 'datasets' / 'tests_fur-elise.mid'
    return str(midi_file_path.resolve())


@pytest.fixture
def npz_file_path(test_dir):
    # npz_file_path = 'datasets/b97c529ab9ef783a849b896816001748.npz'
    npz_file_path = test_dir / '..' / 'datasets' / 'b97c529ab9ef783a849b896816001748.npz'
    return str(npz_file_path.resolve())


@pytest.fixture
def PrettyMIDI_type(midi_file_path):
    # midi_file_path = 'datasets/tests_fur-elise.mid'
    midi_data = pretty_midi.PrettyMIDI(midi_file=midi_file_path)
    return midi_data


@pytest.fixture
def Pianoroll_type(midi_file_path):
    # midi_file_path = 'datasets/tests_fur-elise.mid'
    midi_data = pretty_midi.PrettyMIDI(midi_file=midi_file_path)
    pr = pypianoroll.from_pretty_midi(midi_data)
    return pr


@pytest.fixture
def pitch_metric_names():
    pitch_metric_names = ['pitch_range', 'n_pitches_used', 'n_pitch_classes_used', 'major_scale',
                          'minor_scale', 'pitch_entropy', 'pitch_class_entropy', 'pitch_class_histogram', 'chroma']
    return pitch_metric_names


@pytest.fixture
def rythm_metric_names():
    rythm_metric_names = ['empty_beat_rate', 'drum_in_pattern_rate_duple', 'drum_in_pattern_rate_triple',
                          'drum_pattern_consistency', 'groove_consistency', 'tempo_changes', 'n_times_tempo_change',
                          'end_time', 'estimate_tempi', 'estimate_tempo', 'beats', 'beat_start', 'downbeats', 'n_beats',
                          'onsets', 'n_notes', 'time_signatures', 'n_signatures']
    return rythm_metric_names


@pytest.fixture
def harmonic_metric_names():
    harmonic_metric_names = ['polyphony', 'polyphony_rate', 'pitch_class_transition_matrix', 'tonal_distance']
    return harmonic_metric_names


@pytest.fixture
def table_field_names():
    table_field_names = ['Metric', 'Value', 'Description']
    return table_field_names

# ---------------------------------------------------------


def test_metrics_midi_path(midi_file_path, pitch_metric_names, rythm_metric_names, harmonic_metric_names):
    pitch_metrics_path, _ = get_pitch_metrics(midi_file_path)
    rythm_metric_path, _ = get_rythm_metrics(midi_file_path)
    harmonic_metric_path, _ = get_harmonic_metrics(midi_file_path)

    for pm_name in pitch_metrics_path.keys():
        assert pm_name in pitch_metric_names

    for rm_name in rythm_metric_path.keys():
        assert rm_name in rythm_metric_names

    for hm_name in harmonic_metric_path.keys():
        assert hm_name in harmonic_metric_names


def test_metrics_npz_path(npz_file_path, pitch_metric_names, rythm_metric_names, harmonic_metric_names):
    pitch_metrics_path, _ = get_pitch_metrics(npz_file_path)
    rythm_metric_path, _ = get_rythm_metrics(npz_file_path)
    harmonic_metric_path, _ = get_harmonic_metrics(npz_file_path)

    for pm_name in pitch_metrics_path.keys():
        assert pm_name in pitch_metric_names

    for rm_name in rythm_metric_path.keys():
        assert rm_name in rythm_metric_names

    for hm_name in harmonic_metric_path.keys():
        assert hm_name in harmonic_metric_names


def test_metrics_PrettyMIDI_type(PrettyMIDI_type, pitch_metric_names, rythm_metric_names, harmonic_metric_names):
    pitch_metrics_path, _ = get_pitch_metrics(PrettyMIDI_type)
    rythm_metric_path, _ = get_rythm_metrics(PrettyMIDI_type)
    harmonic_metric_path, _ = get_harmonic_metrics(PrettyMIDI_type)

    for pm_name in pitch_metrics_path.keys():
        assert pm_name in pitch_metric_names

    for rm_name in rythm_metric_path.keys():
        assert rm_name in rythm_metric_names

    for hm_name in harmonic_metric_path.keys():
        assert hm_name in harmonic_metric_names


def test_metrics_Pianoroll_type(Pianoroll_type, pitch_metric_names, rythm_metric_names, harmonic_metric_names):
    pitch_metrics_path, _ = get_pitch_metrics(Pianoroll_type)
    rythm_metric_path, _ = get_rythm_metrics(Pianoroll_type)
    harmonic_metric_path, _ = get_harmonic_metrics(Pianoroll_type)

    for pm_name in pitch_metrics_path.keys():
        assert pm_name in pitch_metric_names

    for rm_name in rythm_metric_path.keys():
        assert rm_name in rythm_metric_names

    for hm_name in harmonic_metric_path.keys():
        assert hm_name in harmonic_metric_names


def test_pitch_metrics_table_midi_path(midi_file_path, table_field_names):
    _, metrics_pitch_table_path = get_pitch_metrics(midi_file_path)
    _, metrics_rythm_table_path = get_rythm_metrics(midi_file_path)
    _, metrics_harmonic_table_path = get_harmonic_metrics(midi_file_path)

    assert metrics_pitch_table_path.field_names == table_field_names
    assert metrics_rythm_table_path.field_names == table_field_names
    assert metrics_harmonic_table_path.field_names == table_field_names
