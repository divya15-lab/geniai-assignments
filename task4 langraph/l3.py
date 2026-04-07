from langgraph.graph import StateGraph
from typing import TypedDict
import ollama

print("===== LG3: Tool Node =====")

# -------------------------------
# State
# -------------------------------
class State(TypedDict):
    input: str
    output: str

# -------------------------------
# Tool: Calculator
# -------------------------------
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

# -------------------------------
# Decision Node
# -------------------------------
def decide_tool(state):
    text = state["input"]

    if any(op in text for op in ["+", "-", "*", "/"]):
        return "tool"
    else:
        return "llm"

# -------------------------------
# Tool Node
# -------------------------------
def tool_node(state):
    text = state["input"]

    # remove words and symbols
    expression = text.replace("What is", "").replace("?", "").strip()

    result = calculator(expression)

    return {"output": result}

# -------------------------------
# LLM Node
# -------------------------------
def llm_node(state):
    text = state["input"]

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': text}]
    )

    return {"output": response['message']['content']}

# -------------------------------
# Build Graph
# -------------------------------
graph = StateGraph(State)

graph.add_node("tool", tool_node)
graph.add_node("llm", llm_node)

graph.add_conditional_edges(
    "__start__",
    decide_tool,
    {
        "tool": "tool",
        "llm": "llm"
    }
)

app = graph.compile()

# -------------------------------
# Test
# -------------------------------
input_text = "What is 25 + 8?"

# Try also:
# input_text = "Explain LangChain"

result = app.invoke({"input": input_text})

print("\nFinal Output:")
print(result["output"])

print("\n===== LG3 Completed =====")
