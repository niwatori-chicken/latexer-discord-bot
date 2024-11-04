# latexer-discord-bot
## 概要
Math-mode LaTeXコードをコンパイルしてpngとして出力するbotです。

## 使い方
`/compile_latex`
Math-modeのLaTeXをコンパイルします。

引数:
- latex_code LaTeXのコードを入力します。
- font_size フォントサイズを入力します。既定値は10です。
- silent Trueを指定すると自分にのみ見えるメッセージとして送信されます。既定値はFalseです。
- font_type フォントの種類を入力します。既定値はcmです。

## 実行
`matplotlib`, `discord.py`, `python-dotenv`モジュールが必要です。pipコマンドでインストールしてください。
トークンは情報の保護のため、`.env`ファイルに格納します。実行したいbotのトークンを、`.env`の中に`TOKEN="(あなたのbotのトークン)"`の形式で書き込んでください。

## ライセンス
Copyright 2024 niwatori-chicken

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
