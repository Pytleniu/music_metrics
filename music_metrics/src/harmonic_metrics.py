import muspy
import pypianoroll
from prettytable import PrettyTable

from .utils import load_representations

def get_harmonic_metrics(data: any):

    muspy_representation, midi_representation, pianoroll_representation = load_representations(data)

    polyphony = polyphony_rate = pitch_class_transition_matrix = tonal_distance = None

    # muspy
    polyphony = muspy.polyphony(music=muspy_representation)
    polyphony_rate = muspy.polyphony_rate(music=muspy_representation)

    # pretty_midi
    # pitch_class_transition_matrix = midi_representation.get_pitch_class_transition_matrix()

    # pypianoroll
    # tonal_distance = pypianoroll.tonal_distance(
    #     pianoroll_1=pianoroll_representation,
    #     pianoroll_2=pianoroll_representation,
    #     resolution=1
    # )

    metrics_table = PrettyTable()
    metrics_table.field_names = ['Metric', 'Value', 'Description']

    metric_descriptions = {
        'polyphony': 'The average number of sounds played at one time. Percussion tracks are not taken into account.',
        'polyphony_rate': 'The ratio of temporal moments in which more than one sound is played to the duration of the entire piece. Provides information about the frequency of polyphony in a given piece.',
        'pitch_class_transition_matrix': 'A transition matrix representing how often each sound class (e.g., C, C#, D, etc.) transitions to another sound class in a song. Used for harmonic analysis of a piece',
        'tonal_distance': 'The tonal distance between the two specified music rolls. The returned value is a floating point number. Tonal distance is used to describe the degree of harmonic and tonal similarity between two pieces of music.',
    }

    harmonic_metrics = {
        'polyphony': polyphony,
        'polyphony_rate': polyphony_rate,
        'pitch_class_transition_matrix': pitch_class_transition_matrix,
        'tonal_distance': tonal_distance,
    }

    for metric, value in harmonic_metrics.items():
        description = metric_descriptions.get(metric, "")
        metrics_table.add_row([metric, value, description])

    return harmonic_metrics, metrics_table