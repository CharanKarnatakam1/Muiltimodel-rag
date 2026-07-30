from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a FAISS vector store from text chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store, save_path="data/faiss_index"):
    """
    Save the FAISS index to disk.
    """

    vector_store.save_local(save_path)


def load_vector_store(save_path="data/faiss_index"):
    """
    Load the FAISS index from disk.
    """

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        folder_path=save_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store