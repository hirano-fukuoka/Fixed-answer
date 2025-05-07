import streamlit as st

st.title("技術検討依頼チェックアプリ")

# アプリ概要の説明をマークダウンで表示
st.markdown("""
### 📘 アプリ概要

このアプリは、質問文に特定のキーワード（例：解析、図面、調査など）が含まれているかを自動判定し、  
**「技術検討依頼書」が必要かどうかを回答する**チェックツールです。

以下のように動作します：

- 質問に「解析」「図面」などのキーワードが含まれている場合：  
  → `〇〇なので技術検討依頼書は必要です。`
- 複数キーワードが含まれている場合：  
  → `〇〇と〇〇なので技術検討依頼書は絶対に必要です。`
- キーワードがない場合：  
  → `ちょっと質問の意味がわかりません。`
""")

# 質問入力欄
user_question = st.text_input("質問を入力してください：")

if user_question:
    question_lower = user_question.lower()
    keywords = ["解析", "図面", "承認図", "製作図", "改造図", "調査", "検討", "分析", "観察"]

    matched_keywords = [kw for kw in keywords if kw in question_lower]

    if matched_keywords:
        if len(matched_keywords) == 1:
            response = f"{matched_keywords[0]}なので技術検討依頼書は必要です。"
        else:
            keyword_str = "と".join(matched_keywords)
            response = f"{keyword_str}なので技術検討依頼書は絶対に必要です。"
    else:
        response = "ちょっと質問の意味がわかりません。"

    st.subheader("回答")
    st.write(response)
