from langchain_ollama import ChatOllama

print("===== L2: Retrieval QA (Real) =====")

# Step 1: Load documents
print("\nStep 1: Loading documents...")
with open("data.txt", "r") as f:
    documents = f.readlines()

print("✔ Documents loaded")

# Step 2: Query
query = "What is LangChain?"
print("\nQuery:", query)

# Step 3: Simple retrieval (search relevant doc)
print("\nStep 2: Retrieving relevant document...")

relevant_doc = ""
for doc in documents:
    if "LangChain" in doc:
        relevant_doc = doc

print("✔ Relevant document found:", relevant_doc.strip())

# Step 4: LLM to generate answer
print("\nStep 3: Sending to LLM...")

llm = ChatOllama(model="llama3")

prompt = f"""
Answer the question based on the context below.

Context:
{relevant_doc}

Question:
{query}
"""

response = llm.invoke(prompt)

print("\nAnswer:", response.content)

print("\n===== L2 Completed =====")
