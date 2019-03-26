# Some Note-worthy Problems
## Keras
### shape problems
rnn input shape = (num_inputs, timesteps, input_dim)
LSTM(input_shape=(timesteps, input_dim))

## Music21
### element attributes
universal: offset
note: note
chord: notes
### extract
for file in glob.glob('./midi_songs/*.mid'):
  midi = converter.parse(file)
  notes_to_parse = instrument.partitionByInstrument(midi).parts[0].recurse()
  for element in notes_to_parse:
    ...
