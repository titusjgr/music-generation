# Some Note-worthy Problems
## Keras
### shape problems
``` python
rnn input shape = (num_inputs, timesteps, input_dim)
LSTM(input_shape=(timesteps, input_dim))
```
## fastai
或許比keras好用，只要把midi正確的轉換成text，然後就可以用內建model

## Music21
### element attributes
universal: offset
note: note
chord: notes
### extract
```python
for file in glob.glob('./midi_songs/*.mid'):
  midi = converter.parse(file)
  notes_to_parse = instrument.partitionByInstrument(midi).parts[0].recurse()
  for element in notes_to_parse:
    ...
```
## posts
http://christinemcleavey.com/clara-a-neural-net-music-generator/

表示方法：把midi轉成text檔案，用note的開始(以12為例)和結束(12end)來標示，所有音都沒有就用(wait)
把開頭塞進list之後紀錄結束時間，用dict把每個結束時間當作key，每當offset到了就把全部end加上

## 問題
有奇怪的節奏，直接用原曲轉換也會出現，發現offset有微妙差異
