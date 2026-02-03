import streamlit as st
import pandas as pd
import altair as alt

data_frames = {}
for month in range(2301, 2313):  # 2401から2408まで
    try:
        sheet_name = str(month)
        df = pd.read_excel("./sales_amount_sample.xlsx", sheet_name=sheet_name, 
                        engine="openpyxl", index_col=0)
        data_frames[sheet_name] = df  # シート名をキーとしてデータフレームを格納
    except ValueError as e:
        pass


# data_framesの各データフレームを行方向に結合
combined_df = pd.concat(data_frames.values(), axis=0, keys=data_frames.keys())

# マルチインデックスのレベル0（シート名）をカラムに戻す
combined_df = combined_df.reset_index(level=0)

# 新しいインデックス（シート名）を設定
combined_df = combined_df.set_index('level_0', append=False)

# インデックスの名前を変更
combined_df.index.name = 'シート名'

# 新たなデータフレームの表示
st.dataframe(combined_df)