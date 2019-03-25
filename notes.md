# 音樂生成20
## 我想傳達
* 現在的發展
* 怎麼玩
* 背後的技術
## 架構
* 背景
  * 作曲
  * ai 作曲
* demo 開跑
* 技術介紹
https://arxiv.org/pdf/1612.01010.pdf
https://arxiv.org/abs/1903.07227
  * 音樂的本質(2)
  * midi(2)
  * 機器學習(3)
  * 循環神經網路(2)
* 播放曲目(2)
* 問題(3)

---

## 背景
開始先撥放aiva的[genesis](https://soundcloud.com/user-95265362/sets/genesis)
### 作曲
音樂創作可以指一首原創樂曲、樂曲的結構或創作新音樂作品的過程。狹義的音樂創作者稱為作曲家，廣義上則包括作詞家與編曲家。
### ai 作曲
和聲：[bach doodle 3/21](https://www.google.com/doodles/celebrating-johann-sebastian-bach)，選幾個音符，給bach風格的合聲<br>
例子，開場時撥放的曲子<br>
有50%的人把deepbach的曲子認成是bach的[mit tech review-Deep-Learning Machine Listens to Bach, Then Writes Its Own Music in the Same Style](https://www.technologyreview.com/s/603137/deep-learning-machine-listens-to-bach-then-writes-its-own-music-in-the-same-style/)，用了352首眾讚歌(chorale)來學習曲風
## 技術介紹
### 音樂元素
wiki
* 節奏
* 旋律：音高序列
* 和聲
* 音色
音色合成也可透過機器進行https://storage.googleapis.com/magentadata/papers/gansynth/interpolations/bach_interpolated.mp3
### midi
midi包含樂器，時長等資料，可以儲存曲子，我用music21來擷取
### 機器學習
建立模型，用資料來自動調整參數，我們用的是一種叫做循環神經網路
### RNN
有記憶的神經網路，每次輸出丟回輸入，用於預測序列、翻譯等

### outer
十二音列、極簡主義
