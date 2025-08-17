# corres-analysis-mir
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


このリポジトリは、**コレスポンデンス分析（Correspondence Analysis）を使って、商品と印象語の関係を可視化するサンプル** をまとめたものです。


このリポジトリは、**コレスポンデンス分析（Correspondence Analysis）を使って、商品と印象語の関係を可視化するサンプル** をまとめたものです。

主に以下のことができます：

- 車ごとの印象ワードの分布を集計
- コレスポンデンス分析で2次元空間にプロット
- 結果をExcelに出力して、報告書やプレゼンに活用可能

> 少ないサンプルデータでも「傾向」をつかむことができ、マーケティングの意思決定に役立てることができます。

---

## 環境
- Python 3.x
- 必要ライブラリ: `pandas`, `numpy`, `prince`, `matplotlib`, `japanize_matplotlib`, `openpyxl`

---

## フォルダ構成

```
├─ 1_flow/
│   └─ corres_analysis.py        # 実行スクリプト
├─ 2_data/
│   └─ sample_car_data.csv       # サンプルデータ
├─ 3_output/                     # データ出力先（自動作成）
```

---
# 入力データフォーマット例
2_data/sample.csv を参照ください。


## 使い方

### 1. CSVを準備
`2_data/sample_car_data.csv` にモニターの回答データを置きます。

### 2. スクリプト実行
```bash
python 1_flow/corres_analysis.py
```
### 3. 処理内容
‐ 自動で集計・行列変換・コレスポンデンス分析・散布図作成・Excel出力まで行います。  
‐ 結果は `3_output/` に保存されます。  

---

## 今後の拡張予定

- 本リポジトリは現在、サンプルデータ（印象分析）向けに対応しています。
- 今後は、より使いやすく、幅広い用途に対応できるように進化予定です。

### 精度・機能の向上
- データ整形や集計の精度向上
- 可視化のカスタマイズ性向上
- 分析対象や辞書・ラベルの自由な拡張

### 分析対象の拡張（例）
- 他の商品カテゴリの印象分析への対応
- アンケートやレビューの自由な分析
- ※ 現在は車サンプルのみ対応
- ※ 拡張版は順次リリース予定で、READMEやリポジトリ内で随時更新

---

## 貢献方法

プロジェクトへの貢献は以下の方法で歓迎します：

- バグ報告や機能追加の提案は **Issues** を通じて  
- コード改善や新機能の追加は **Pull Request** を作成  
- ドキュメントの改善や翻訳も歓迎

---

## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)










