import fitz
from src.chunker import create_chunks


def load_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


if __name__ == "__main__":

    pdf_path = "uploads/sample_company_report.pdf"

    text = load_pdf(pdf_path)

    chunks = create_chunks(text)

    print(f"Total Chunks: {len(chunks)}")

    print("=" * 50)

    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i+1}\n")

        print(chunk)

        print("=" * 50)