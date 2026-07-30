import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from src.retriever import retrieve_documents

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the user's question only using the provided context.

If the answer is not found in the context, reply:
"I couldn't find that information in the document."

Context:
{context}

Question:
{question}

Answer:
""")


def generate_answer(question):
    """
    Generate an answer using RAG.
    """

    # Retrieve relevant documents
    docs = retrieve_documents(question)

    # Combine document text
    context = "\n\n".join([doc.page_content for doc in docs])

    # Create prompt
    messages = prompt.format_messages(
        context=context,
        question=question
    )

    # Generate answer
    response = llm.invoke(messages)

    return response.content


if __name__ == "__main__":

    while True:

        question = input("\nAsk a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = generate_answer(question)

        print("\nAnswer:\n")
        print(answer)