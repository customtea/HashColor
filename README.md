# HashColor

ひと目でハッシュ値がわかる？

## 概要
ハッシュ生成したものを画像で表示するだけ  
SHA256で生成された16進数64文字を使い、8x8のマスに左上から右下にかけて埋める。(1セル80pixelの640x640のサイズで画像出力)

## 色について
- 16進数を単純に16色のパレットで変換する。
- 使用するパレットはHTML4.0で規定されたもの OldColor
- [Colors](http://clrs.cc/) のサイトで提供されるモダンな16色（オレンジを除く）を利用したModernColor
- 16段階のグレースケールでの出力 grayscale

## 使用ライブラリ
- hashlib ハッシュ生成

2種の実装系
- OpenCV系
  - OpenCV
  - Numpy
- PIL系
  - Pillow
    - `pip install pillow`


## hashcolorのプログラム
- `$ python hashcolor [Text]`
- `-f` 入力された\[Text\]をファイルとして解釈して読み込む
- `-t` 出力形式を選択
  - m ModernColor
  - o OldColor
  - g Grayscale
- `-s` 指定したファイル名で出力を保存する。画像の表示はしない


## todo
- SilverとWhiteの違いが分かりづらい気がする。 特にModenの方
- オレオレ仕様コマンドライン引数をなおす？