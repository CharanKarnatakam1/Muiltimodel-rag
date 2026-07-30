import streamlit as st
import os

from src.loader import load_pdf
from src.chunker import create_chunks
from src.vector_store import create_vector_store, save_vector_store
from src.rag import generate_answer

st.set_page_config(
    page_title="Multimodal RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Multimodal RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF Uploaded Successfully")

    with st.spinner("Processing PDF..."):

        text = load_pdf(file_path)

        chunks = create_chunks(text)

        vector_store = create_vector_store(chunks)

        save_vector_store(vector_store)

    st.success("✅ PDF Indexed Successfully")

    question = st.text_input("Ask a Question")

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("Generating Answer..."):

                answer = generate_answer(question)

            st.subheader("Answer")

            st.write(answer)

        else:
            st.warning("Please enter a question.")