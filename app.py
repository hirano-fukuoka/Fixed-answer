import streamlit as st

st.title("技術検討依頼チェックアプリ")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

if user_question:
    question_lower = user_question.lower()
    
    # キーワード一覧（新たに3語追加）
    keywords = ["解析", "図面", "承認図", "製作図", "改造図", "調査", "検討", "分析", "観察"]

    # マッチしたキーワードを抽出
    matched_keywords = [kw for kw in keywords if kw in question_lower]

    if matched_keywords:
        if len(matched_keywords) == 1:
            response = f"{matched_keywords[0]}なので技術検討依頼書は必要です。"
        else:
            # 「と」でキーワードを連結（例：解析と図面）
            keyword_str = "と".join(matched_keywords)
            response = f"{keyword_str}なので技術検討依頼書は絶対に必要です。"
    else:
        response = "ちょっと質問の意味がわかりません。"

    st.subheader("回答")
    st.write(response)
