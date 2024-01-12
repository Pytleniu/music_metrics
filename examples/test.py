import music_metrics
import pretty_midi
import pypianoroll
import os
from pathlib import Path

script_dir = Path(os.path.dirname(os.path.abspath(__file__)))

MIDI_FILE_PATH = script_dir / '..' / 'datasets' / 'tests_fur-elise.mid'
PR_FILE_PATH = script_dir / '..' / 'datasets' / 'b97c529ab9ef783a849b896816001748.npz'

MIDI_FILE_PATH = str(MIDI_FILE_PATH.resolve())
PR_FILE_PATH = str(PR_FILE_PATH.resolve())

midi_data = pretty_midi.PrettyMIDI(midi_file=MIDI_FILE_PATH)
pr = pypianoroll.from_pretty_midi(midi_data)


# path test
pitch_metrics_path, metrics_pitch_table_path = music_metrics.get_pitch_metrics(
    MIDI_FILE_PATH)
rythm_metrics_path, metrics_rythm_table_path = music_metrics.get_rythm_metrics(
    MIDI_FILE_PATH)
harmonic_metrics_path, metrics_harmonic_table_path = music_metrics.get_harmonic_metrics(
    MIDI_FILE_PATH)

# midi test
pitch_metris_midi, metrics_pitch_table_midi = music_metrics.get_pitch_metrics(
    midi_data)
rythm_metrics_midi, metrics_rythm_table_midi = music_metrics.get_rythm_metrics(
    midi_data)
harmonic_metrics_midi, metrics_harmonic_table_midi = music_metrics.get_harmonic_metrics(
    midi_data)

# pianoroll test
pitch_mertics_pianoroll, metrics_pitch_table_pianoroll = music_metrics.get_pitch_metrics(
    pr)
rythm_metrics_pianoroll, metrics_rythm_table_pianoroll = music_metrics.get_rythm_metrics(
    pr)
harmonic_metrics_pianoroll, metrics_harmonic_table_pianoroll = music_metrics.get_harmonic_metrics(
    pr)

histogram = pitch_metrics_path['pitch_class_histogram']
music_metrics.plot_pitch_class_histogram(histogram)
