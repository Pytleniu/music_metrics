import muspy
import pypianoroll
from prettytable import PrettyTable

from utils import load_representations

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
        'polyphony': '',
        'polyphony_rate': '',
        'pitch_class_transition_matrix': '',
        'tonal_distance': '',
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