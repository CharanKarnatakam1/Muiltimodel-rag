from src.vector_store import load_vector_store


def retrieve_documents(query, k=3):
    """
    Retrieve the top-k relevant chunks from the FAISS vector store.
    """

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(query, k=k)

    return docs


if __name__ == "__main__":

    question = input("Enter your question: ")

    documents = retrieve_documents(question)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(documents, start=1):
        print(f"Chunk {i}")
        print("-" * 50)
        print(doc.page_content)
        print()