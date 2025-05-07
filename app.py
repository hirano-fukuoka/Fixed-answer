import streamlit as st

st.title("技術検討依頼 質問アプリ")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

# 質問が入力されたら固定の回答を表示
if user_question:
    st.subheader("回答")
    st.write("技術検討依頼書は必要です。")
