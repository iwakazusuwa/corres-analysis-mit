# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
#=============================================
# 必要ライブラリ
#=============================================
import pandas as pd
import numpy as np
import os
import sys
import subprocess
import prince  # Correspondence Analysis
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

import japanize_matplotlib  # 日本語対応

#=============================================
# 調査の車両数
#=============================================
num_car = 3

#=============================================
# Inputファイル情報
#=============================================
INPUT_folder = "2_data"
INPUT_DNAME = "sample_car_data.csv"

#=============================================
# Outputファイル情報
#=============================================
OUTPUT_folder = "3_output"
OUTPUT_DNAME = "1_平均.csv"
OUTPUT_DIS = "2_行列入れ替え.csv"
OUTPUT_AVE = "3_コレポンデータ.xlsx"

#=============================================
# パス設定
#=============================================
parent_path = os.path.dirname(os.getcwd())
input_path = os.path.join(parent_path, INPUT_folder, INPUT_DNAME)
output_path = os.path.join(parent_path, OUTPUT_folder)
os.makedirs(output_path, exist_ok=True)

save_name_1 = os.path.join(output_path, OUTPUT_DNAME)
save_name_2 = os.path.join(output_path, OUTPUT_DIS)
save_name_3 = os.path.join(output_path, OUTPUT_AVE)

#=============================================
# CSV読み込み
#=============================================
try:
    df = pd.read_csv(input_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(input_path, encoding="cp932")


# 列名確認
print("Columns:", ", ".join(df.columns))

# %%
# 列名確認
print("Columns:", ", ".join(df.columns))

# =============================================
# Car列セットの開始インデックスを取得
# =============================================
car_indices = [i for i, col in enumerate(df.columns) if col.startswith("Car")]
car_indices.append(len(df.columns))

# =============================================
# Car列セットごとにデータを抽出して縦連結
# =============================================
dfs = []
for idx in range(len(car_indices)-1):
    start = car_indices[idx]
    end = car_indices[idx+1]
    cols = [df.columns[0]] + list(df.columns[start:end])
    temp_df = df[cols].copy()
    # 列名を統一
    temp_df.columns = ['ID', 'Car', 'Elegant', 'Luxurious', 'Sporty', 'Technology',
                       'Futuristic', 'Traditional', 'Cute', 'Cool', 'Sleek', 'Trendy']
    dfs.append(temp_df)

df_long = pd.concat(dfs, axis=0, ignore_index=True)
df_long.to_csv("1.csv", encoding='cp932', index=False)
df_long.head(3)

# %%
#=============================================
# イメージワードの開始列を指定（ID列とCar列以降の列）
#=============================================
image_cols = df_long.columns[2:]

# NaNを空文字に置換
df_long[image_cols] = df_long[image_cols].fillna('')

# "1"（文字）または1（数値）を1に、それ以外は0に変換
df_long[image_cols] = df_long[image_cols].applymap(lambda x: 1 if x == 1 or x == '1' else 0)

df_long[image_cols] .head(3)

# %%
# Carごとに平均値を算出
df_grouped = df_long.groupby('Car')[image_cols].mean().reset_index()
df_grouped.to_csv(save_name_1, index=False, encoding='utf-8-sig')


# 行列入れ替え
data = df_grouped.set_index('Car').T
data.to_csv(save_name_2, index=True, encoding='utf-8-sig')


# %%
# =============================================
# コレスポンデンス分析
# =============================================
data_c = data.copy()
ca = prince.CA(n_components=2, n_iter=10, copy=True, check_input=True, engine='sklearn')
ca = ca.fit(data_c)
row_coords = ca.row_coordinates(data_c)
col_coords = ca.column_coordinates(data_c)

# %%
# =============================================
# プロット
# =============================================
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(row_coords[0], row_coords[1], color='blue', label='Impression')
for i, txt in enumerate(row_coords.index):
    ax.annotate(txt, (row_coords.iloc[i,0], row_coords.iloc[i,1]), color='blue')

ax.scatter(col_coords[0], col_coords[1], color='red', label='Car')
for i, txt in enumerate(col_coords.index):
    ax.annotate(txt, (col_coords.iloc[i,0], col_coords.iloc[i,1]), color='red')

ax.axhline(0, color='grey', linewidth=0.5)
ax.axvline(0, color='grey', linewidth=0.5)
ax.set_title('Correspondence Analysis: Car Brands and Impressions')
ax.legend()
plt.show()

# =============================================
# 結果をCSV出力
# =============================================
col_coords['type'] = 'Car'
row_coords['type'] = 'Impression'
combined = pd.concat([col_coords, row_coords])
#combined.to_csv(save_name_3, index=False, encoding='utf-8-sig')
combined.to_excel(save_name_3, index=False, engine='openpyxl')
print(combined)

# =============================================
# 出力フォルダを開く
# =============================================
if sys.platform.startswith('win'):
    os.startfile(output_path)
elif sys.platform.startswith('darwin'):
    subprocess.run(['open', output_path])
else:
    subprocess.run(['xdg-open', output_path])

print("完了")

# %%

# %%
