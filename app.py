import streamlit as st

st.title("技術検討依頼チェックアプリ")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

# 回答表示
if user_question:
    question_lower = user_question.lower()
    keywords = ["解析", "図面", "承認図", "製作図", "改造図", "調査"]

    # マッチするキーワードのリストを抽出
    matched_keywords = [kw for kw in keywords if kw in question_lower]

    if matched_keywords:
        # 最初に見つかったキーワードで回答を構成
        response = f"{matched_keywords[0]}なので技術検討依頼書は必要です。"
    else:
        response = "ちょっと質問の意味がわかりません。"

    st.subheader("回答")
    st.write(response)
