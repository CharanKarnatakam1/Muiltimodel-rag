from src.embeddings import get_embedding_model

embedding = get_embedding_model()

text = "What is Artificial Intelligence?"

vector = embedding.embed_query(text)

print(f"Vector Length: {len(vector)}")
print(vector[:10])   # Print first 10 values