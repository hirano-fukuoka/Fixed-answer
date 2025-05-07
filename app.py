import streamlit as st

st.title("技術検討依頼チェックアプリ")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

# 回答表示
if user_question:
    # キーワードチェック（小文字化して判定）
    question_lower = user_question.lower()
    if "解析" in question_lower or "図面" in question_lower:
        response = "技術検討依頼書は必要です。"
    else:
        response = "ちょっと質問の意味がわかりません。"

    st.subheader("回答")
    st.write(response)
