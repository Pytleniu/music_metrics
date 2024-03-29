import pypianoroll
import pretty_midi
import muspy
import music21
from functools import singledispatch
import os


@singledispatch
def load_representations(data):
    """
    Load musical data into various representations.

    This function is a single-dispatch generic function that converts input musical data
    into different formats depending on its type. It supports formats like MIDI, MusicXML,
    and NPZ, and converts them into muspy, pretty_midi, and pypianoroll representations.

    Parameters
    ----------
    data : various types
        The input musical data which can be in various formats such as file paths,
        pretty_midi.PrettyMIDI objects, music21.stream objects, etc.

    Returns
    -------
    tuple
        A tuple containing up to three elements based on the input data type:
            1. muspy representation
            2. pretty_midi representation
            3. pypianoroll representation
    """
    return data, data, data


@load_representations.register
def _(data: str):
    _, extension = os.path.splitext(data)
    extension = extension.lower()

    if extension in ['.mid', '.midi']:
        midi_representation = pretty_midi.PrettyMIDI(data)
        muspy_representation = muspy.from_pretty_midi(midi_representation)
        pianoroll_representation = midi_representation.get_piano_roll()
        return muspy_representation, midi_representation, pianoroll_representation
    elif extension in ['.xml', '.musicxml']:
        muspy_representation = muspy.inputs.read_musicxml(data)
        midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
        pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
        return muspy_representation, midi_representation
    elif extension == '.npz':
        pianoroll_representation = pypianoroll.load(data)
        muspy_representation = muspy.from_pypianoroll(pianoroll_representation)
        midi_representation = muspy.to_pretty_midi(muspy_representation)
        return muspy_representation, midi_representation, pianoroll_representation
    else:
        raise ValueError(f'Unsupported file type: {extension}')


@load_representations.register
def _(data: pypianoroll.Multitrack):
    muspy_representation = muspy.inputs.from_pypianoroll(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    return muspy_representation, midi_representation, data


@load_representations.register
def _(data: pypianoroll.Track):
    muspy_representation = muspy.inputs.from_pypianoroll_track(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    return muspy_representation, midi_representation, data


@load_representations.register
def _(data: pretty_midi.PrettyMIDI):
    muspy_representation = muspy.inputs.from_pretty_midi(data)
    pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
    return muspy_representation, data, pianoroll_representation


@load_representations.register
def _(data: music21.stream.Stream):
    muspy_representation = muspy.inputs.from_music21(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
    return muspy_representation, midi_representation, pianoroll_representation


@load_representations.register
def _(data: music21.stream.Opus):
    muspy_representation = muspy.inputs.from_music21_opus(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
    return muspy_representation, midi_representation, pianoroll_representation


@load_representations.register
def _(data: music21.stream.Part):
    muspy_representation = muspy.inputs.from_music21_part(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
    return muspy_representation, midi_representation, pianoroll_representation


@load_representations.register
def _(data: music21.stream.Score):
    muspy_representation = muspy.inputs.from_music21_score(data)
    midi_representation = muspy.outputs.to_pretty_midi(muspy_representation)
    pianoroll_representation = muspy.outputs.to_pypianoroll(muspy_representation)
    return muspy_representation, midi_representation, pianoroll_representation
