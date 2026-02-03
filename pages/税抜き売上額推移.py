import streamlit as st
import pandas as pd
import altair as alt

# 既存のコード
xls = pd.ExcelFile('sales_amount_sample.xlsx')
sheet_names = xls.sheet_names
dfs = {sheet_name: pd.read_excel(xls, sheet_name) for sheet_name in sheet_names}

# 新しいデータフレームを作成するための準備
data = []

# 各シートのデータから「税抜売上額」カラムを選択し、リストに追加
for sheet_name, df in dfs.items():
  if '税抜売上額' in df.columns:
    # 「税抜売上額」カラムのデータを取得し、シート名をカラム名として設定
    temp_df = df[['税抜売上額']].copy()
    temp_df.columns = [sheet_name]
    data.append(temp_df)

# 全てのシートのデータを結合
# axis=1は列方向の結合を意味し、sort=Falseは結合時にインデックスをソートしないことを意味します
combined_df = pd.concat(data, axis=1, sort=False)

# combined_df の行と列を入れ替える
transposed_df = combined_df.transpose()

st.dataframe(combined_df)
st.line_chart(transposed_df)

