import streamlit as st

st.title("技術検討依頼チェックアプリ")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

# 回答表示
if user_question:
    # 小文字に変換して判定しやすくする
    question_lower = user_question.lower()
    
    # キーワードリスト（必要に応じて追加可能）
    keywords = ["解析", "図面", "承認図", "製作図", "改造図", "調査"]
    
    # いずれかのキーワードが含まれているかを判定
    if any(keyword in question_lower for keyword in keywords):
        response = "技術検討依頼書は必要です。"
    else:
        response = "ちょっと質問の意味がわかりません。"

    st.subheader("回答")
    st.write(response)
