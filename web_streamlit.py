import streamlit as st
import httpx

st.title("Qwen2.5 RAG 聊天助手")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("请输入你的问题..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        # 创建一个空占位符，用于流式更新
        message_placeholder = st.empty()
        full_response = ""
        
        with httpx.Client() as client:
            with client.stream("GET", "http://localhost:6066/chat", params={"message": prompt}) as response:
                for chunk in response.iter_text():
                    full_response += chunk
                    # 只更新占位符内容，不新增行
                    message_placeholder.markdown(full_response + "▌")
        # 最后去掉光标
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})