import streamlit as st
import pandas as pd
import altair as alt

# エクセルファイルからデータを読み込む
data_frames = {}
for month in range(2401, 2413):  # 2401から2412まで
  sheet_name = str(month)
  try:
    df = pd.read_excel("./item_sales_sample.xlsx", sheet_name=sheet_name, 
               engine="openpyxl", index_col=0)
    data_frames[sheet_name] = df  # シート名をキーとしてデータフレームを格納
  except ValueError as e:
    pass

# 集計用の空のデータフレームを作成
aggregated_df = pd.DataFrame()

# 各シートのデータを処理
for sheet_name, df in data_frames.items():
  # 項目名でグループ化し、数量を集計
  aggregated_data = df.groupby('項目名')['数量'].sum().reset_index()
  
  # シート名を新しいカラムとして追加し、そのカラムに数量を設定
  aggregated_data['シート名'] = sheet_name
  
  # 項目名をインデックスに、シート名をカラムに、数量を値に設定
  pivot_df = aggregated_data.pivot(index='項目名', columns='シート名', values='数量')
  
  # 集計用データフレームに結合
  aggregated_df = pd.concat([aggregated_df, pivot_df], axis=1)

# NaNを0で埋める
aggregated_df.fillna(0, inplace=True)

# '取引合計'と'その他'の行を削除
aggregated_df = aggregated_df.drop(['※　取引合計　※', 'その他'], axis=0)

# '海鮮'の行の中央値を計算
median_seafood = aggregated_df.loc['海鮮'].median()
# 2401と2405のカラムにおいて、'海鮮'の行を中央値で更新
aggregated_df.loc['海鮮', ['2401', '2405']] = median_seafood


# 関数の定義
def monthly_set_sales():
  col_1, col_2 = st.columns(2)
  with col_1:
    selected_month = st.radio("月を選んでください",
                                  aggregated_df.columns.values,  # 月名を取得したリスト
                                  key="set_sales01")
  with col_2:
    st.write("選んだ月の品目ごとの数量の棒グラフ")
    # マルチセレクトで品目を選択
    selected_items = st.multiselect("品目を選んでください（複数選択可）", 
                                    aggregated_df.index,
                                    ["Aランチ", "Bランチ", "たっぷり定食", "カルビ定食", "ロース定食", "上カルビ定食", "ホルモン定食"],
                                    key="set_sales02")
    # 選択された品目のデータをフィルタリング
    if selected_items:  # 選択された品目がある場合
        filtered_data = aggregated_df.loc[selected_items, selected_month]
        st.bar_chart(filtered_data)
    else:
        st.error("品目が選択されていません")

def monthly_meat_sales():
  col_1, col_2 = st.columns(2)
  with col_1:
    selected_month = st.radio("月を選んでください",
                                  aggregated_df.columns.values,  # 月名を取得したリスト
                                  key="meat_sales01")
  with col_2:
    st.write("選んだ月の品目ごとの数量の棒グラフ")
    # マルチセレクトで品目を選択
    selected_items = st.multiselect("品目を選んでください（複数選択可）", 
                                    aggregated_df.index,
                                    ["カルビ", "ロース", "ハラミ", "タン塩", "上カルビ", "上ロース", "トモサンカク"],
                                    key="meat_sales02")
    # 選択された品目のデータをフィルタリング
    if selected_items:  # 選択された品目がある場合
        filtered_data = aggregated_df.loc[selected_items, selected_month]
        st.bar_chart(filtered_data)
    else:
        st.error("品目が選択されていません")

def monthly_alchole_sales():
  col_1, col_2 = st.columns(2)
  with col_1:
    selected_month = st.radio("月を選んでください",
                                  aggregated_df.columns.values,  # 月名を取得したリスト
                                  key="alchole_sales01")
  with col_2:
    st.write("選んだ月の品目ごとの数量の棒グラフ")
    # マルチセレクトで品目を選択
    selected_items = st.multiselect("品目を選んでください（複数選択可）",
                                    aggregated_df.index,
                                    ["生大", "生中", "生小", "ﾁｭｰﾊｲ ｻﾜｰ", "ﾒｶﾞﾁｭｰﾊｲ ﾒｶﾞｻﾜｰ", "ﾒｶﾞﾊｲﾎﾞｰﾙ", "ハイボール"],
                                    key="alchole_sales02")
    # 選択された品目のデータをフィルタリング
    if selected_items:  # 選択された品目がある場合
        filtered_data = aggregated_df.loc[selected_items, selected_month]
        st.bar_chart(filtered_data)
    else:
        st.error("品目が選択されていません")

def monthly_others_sales():
  col_1, col_2 = st.columns(2)
  with col_1:
    selected_month = st.radio("月を選んでください",
                                  aggregated_df.columns.values,  # 月名を取得したリスト
                                  key="others_sales01")
  with col_2:
    st.write("選んだ月の品目ごとの数量の棒グラフ")
    # マルチセレクトで品目を選択
    selected_items = st.multiselect("品目を選んでください（複数選択可）", 
                                    aggregated_df.index,
                                    key="others_sales02")
    # 選択された品目のデータをフィルタリング
    if selected_items:  # 選択された品目がある場合
        filtered_data = aggregated_df.loc[selected_items, selected_month]
        st.bar_chart(filtered_data)
    else:
        st.error("品目が選択されていません")

def selected_item_mount():
  selected_item = st.multiselect("品目を選んでください（複数選択可）", 
                                    aggregated_df.index,
                                    key=3)
  # 選択された項目名に基づいて、列2401から列2408までのデータを抽出
  selected_item_data = aggregated_df.loc[selected_item, '2401':]

  if selected_item:  # 選択された品目がある場合
    st.dataframe(selected_item_data.transpose())
    st.line_chart(selected_item_data.transpose())
  else:
    st.error("品目が選択されていません")


# expanderで表示
"""
### 1年分の売り上げ個数
"""
with st.expander("詳細を見る"):
  # 全体の集計結果を表示
  st.dataframe(aggregated_df)
  # 全体の棒グラフを表示
  st.bar_chart(aggregated_df)

"""
### 定食の売り上げ個数
"""
with st.expander("詳細を見る"):
  monthly_set_sales()

"""
### 正肉の売り上げ個数
"""
with st.expander("詳細を見る"):
  monthly_meat_sales()

"""
### アルコールの売り上げ個数
"""
with st.expander("詳細を見る"):
  monthly_alchole_sales()

"""
### その他商品の売り上げ個数
"""
with st.expander("詳細を見る"):
  monthly_others_sales()

"""
### 月別の売り上げ個数の推移
"""
with st.expander("詳細を見る"):
  selected_item_mount()

