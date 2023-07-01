import streamlit as st
import os
st.set_page_config(page_title="privateGPT", page_icon="💬", layout="wide")
st.title("Private GPT: Ask questions to your documents.")
# header of the page
st.header("Chat with your documents")
# add side bar
with st.sidebar:
    st.subheader("Your Documents")
    files = st.file_uploader('Upload your documents', type=['pdf', 'txt', 'docx', 'doc', 'pptx', 'ppt', 'csv','enex','eml','epub','html','md','odt',], accept_multiple_files=True, key="upload")
    # save the uploaded files in source_documents folder
    if files:
        for file in files:
            with open(os.path.join("source_documents", file.name), "wb") as f:
                f.write(file.getbuffer())