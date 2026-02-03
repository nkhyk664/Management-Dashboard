import streamlit as st

#タイトル
st.markdown(" ### たいかろう売り上げ分析ダッシュボード")
#キャプション
st.caption("今後の戦略に役立てるために、売り上げデータを分析します。")

"""
### このダッシュボードの使い方
"""
with st.expander("詳細を見る"):
  st.write("自由に選択して調べたい項目のデータをみることができます。")
  st.write("複数選択可能のところは、直接商品名を入力して検索することもできます。")
  st.markdown("<span style='color: red;'>ただし、半角と全角は区別されますので入力するときは注意してください！</span>", unsafe_allow_html=True)

# 集計内容の表示
"""
### 会計集計表の項目
"""
with st.expander("詳細を見る"):
  st.write("037:純売上額")
  st.write("039:内消費税")
  st.write("040:内軽減消費税")
  st.write("043:税抜売上額")
  st.write("073:総売上額")
  st.write("074:取引回数")

"""
### 品目別取引集計表の項目
"""

with st.expander("詳細を見る"):
  st.write("005:項目名")
  st.write("007:取引回数")
  st.write("008:数量")
  st.write("009:金額")
  st.write("016:構成比")