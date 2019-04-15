from fastai.text import load_data, language_model_learner, AWD_LSTM
from fractions import Fraction
from music21 import note, stream, instrument
import time


def predict_notes():
    text_dir = './midi_text'

    data_lm = load_data(text_dir, 'data_lm_export.pkl')

    learner = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)
    learner.load_encoder('AWD_LSTM')

    predicted_notes = learner.predict('', n_words=2500)

    return predicted_notes


def str_to_output(predicted_notes):
    notes_list = predicted_notes.replace('+', '#').replace('_', '/').split(' ')

    starts = {}  # note: offset
    output_notes = []
    offset = Fraction('0')

    for element in notes_list:
        # print(element)
        if element.startswith('wait'):
            offset += float(Fraction(element[4:]))
    #         print('wait')

        elif element.endswith('end') and element[:-3] in starts:
            n = note.Note(element[:-3])
            n.offset = starts[element[:-3]]
            n.quarterLength = offset - n.offset
            n.storedInstrument = instrument.Piano()
            output_notes.append(n)
        else:
            starts[element] = offset

    output_notes = sorted(output_notes, key=lambda n: n.offset)
    # print('output_notes', output_notes)
    return output_notes


def main():
    predicted_notes = predict_notes()
    output_notes = str_to_output(predicted_notes)

    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp='{:.0f}test_output.mid'.format(time.time()))


main()
