from langchain_community.llms import Ollama
import streamlit as st
llm=Ollama(model="llama3.1:latest")
st.title("QnA Chatbot based on Llama3.1(8b)")
prompt=st.text_area("Enter your prompt:")
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))

