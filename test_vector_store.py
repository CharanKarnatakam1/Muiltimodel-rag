from src.loader import load_pdf
from src.chunker import create_chunks
from src.vector_store import create_vector_store, save_vector_store

# Load PDF
text = load_pdf("uploads/sample_company_report.pdf")

# Create Chunks
chunks = create_chunks(text)

print(f"Total Chunks: {len(chunks)}")

# Create Vector Store
vector_store = create_vector_store(chunks)

# Save FAISS Index
save_vector_store(vector_store)

print("✅ FAISS Vector Store Created Successfully!")