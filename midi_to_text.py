from fractions import Fraction
from music21 import converter, note, chord, instrument
import glob
import time
import os


def notes_to_string(notes, filename):
    ''' Transfor the notes into a long string to use fastai library'''
    print('Start parsing', filename)
    start_time = time.time()

    def insert_ends(pitch, quarterLength):
        endtime = current_offset + quarterLength
        if endtime in ends:
            ends[endtime].append(pitch + 'end')
        else:
            ends[endtime] = [pitch + 'end']

    current_offset = Fraction('0')
    notes_list = []
    ends = {}

    for element in notes:
        if element.offset > current_offset:
            while len(ends) != 0 and min(ends.keys()) <= element.offset:
                notes_list.append('wait' + str(min(ends.keys()) - Fraction(current_offset)))
                current_offset = min(ends.keys())
                for pitch in ends[current_offset]:
                    notes_list.append(pitch)
                ends.pop(current_offset)

            notes_list.append('wait' + str(Fraction(element.offset - current_offset)))
            current_offset = Fraction(element.offset)

        if isinstance(element, note.Note):
            # print(element.pitch, element.offset, element.quarterLength)
            notes_list.append(element.pitch.nameWithOctave)
            insert_ends(element.pitch.nameWithOctave, Fraction(element.quarterLength))

        elif isinstance(element, chord.Chord):
            # print('chord', element.pitches, element.offset, element.quarterLength)
            for pitch in element.pitches:
                notes_list.append(pitch.nameWithOctave)
                insert_ends(pitch.nameWithOctave, Fraction(element.quarterLength))

    while len(ends) != 0:
        notes_list.append('wait' + str(min(ends.keys()) - Fraction(current_offset)))
        current_offset = min(ends.keys())
        for pitch in ends[current_offset]:
            notes_list.append(pitch)
        ends.pop(current_offset)

    print('It took %d seconds' % (time.time() - start_time))
    # Avoid the use of special characters
    return ' '.join(notes_list).replace('#', '+').replace('/', '_')


def save_notes_str(text_dir, train, filename):
    fname_no_extension = os.path.splitext(os.path.split(filename)[-1])[0]
    if train == True:
        path = text_dir + '/train/' + fname_no_extension + '.txt'
    else:
        path = text_dir + '/valid/' + fname_no_extension + '.txt'
    f = open(path, 'w', encoding='utf-8')
    f.write(notes_str)
    f.close()


song_dir = './midi_songs'
text_dir = './midi_text'

for i, filename in enumerate(glob.glob(song_dir + '/*.mid')):
    midi = converter.parse(filename)
    notes = instrument.partitionByInstrument(midi).parts[0].recurse()

    notes_str = notes_to_string(notes, filename)

    save_notes_str(text_dir, True, filename)
    if i == 0:
        save_notes_str(text_dir, False, filename)
