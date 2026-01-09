from src.agent import perguntar_ollama
import streamlit as st

st.title("🎓 James, o Especialista em Finanças")


if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar_ollama(pergunta))