import muspy
import music21
import pypianoroll
import pretty_midi
import partitura


# MusPy test
music = muspy.load("test.json")
music.print()

# Music21 test
print(music21.note.Note("F5"))

# pypianoroll test
multitrack = pypianoroll.read("tests_fur-elise.mid")
print(multitrack)

# pretty_midi test
midi_data = pretty_midi.PrettyMIDI('tests_fur-elise.mid')
print(midi_data.estimate_tempo())

# partitura test
midi_data = partitura.load_score_midi('tests_fur-elise.mid')
print(midi_data.id)
