from langchain_ollama import ChatOllama

print("===== L3: Tool Integration (Real) =====")

# -------------------------------
# Tool: Calculator
# -------------------------------
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

# -------------------------------
# LLM Setup
# -------------------------------
llm = ChatOllama(model="llama3")

# -------------------------------
# User Query
# -------------------------------
query = "What is 12 + 8?"

print("\nUser Query:", query)

# -------------------------------
# Step 1: LLM decides tool
# -------------------------------
decision_prompt = f"""
You are an AI.

If the user query is a math question, respond ONLY with:
USE_CALCULATOR

Otherwise respond ONLY with:
NORMAL

Query: {query}
"""

decision = llm.invoke(decision_prompt).content.strip()

print("\nLLM Decision:", decision)

# -------------------------------
# Step 2: Tool usage
# -------------------------------
if "USE_CALCULATOR" in decision:

    # Ask LLM to extract expression
    extract_prompt = f"""
Extract only the mathematical expression from this query.

Query: {query}

Output only the expression (example: 12+8)
"""

    expression = llm.invoke(extract_prompt).content.strip()

    print("\nExtracted Expression:", expression)

    result = calculator(expression)

    print("\nTool Used: Calculator")
    print("Answer:", result)

else:
    response = llm.invoke(query)
    print("\nAnswer:", response.content)

print("\n===== L3 Completed =====")
