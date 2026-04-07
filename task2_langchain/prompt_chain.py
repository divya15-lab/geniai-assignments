from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

print("===== L1: Prompt Chain =====")

# Prompt
prompt = PromptTemplate.from_template(
    "Summarize this text in one line: {text}"
)

# LLM
llm = ChatOllama(model="llama3")

# Chain
chain = prompt | llm

# Input
input_text = "LangChain is a framework for building applications using large language models."

print("\nInput:", input_text)

# Run
result = chain.invoke({"text": input_text})

print("\nOutput:", result.content)

print("\n===== L1 Completed =====")
