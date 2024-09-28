import streamlit as st 

st.title("AI-Chat")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "How can i help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_prompt := st.chat_input():
    st.chat_message("user").write(user_prompt)
    st.session_state.messages = [{"role": "user", "content": user_prompt}]