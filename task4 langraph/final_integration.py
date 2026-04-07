from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph
from typing import TypedDict
import ollama

print("===== FINAL INTEGRATION PROJECT =====")

app = FastAPI()

# -------------------------------
# Request Model
# -------------------------------
class Query(BaseModel):
    query: str

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
# Build LangGraph
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

agent = graph.compile()

# -------------------------------
# API Endpoint
# -------------------------------
@app.post("/ask")
def ask(query: Query):
    print("Received Query:", query.query)

    result = agent.invoke({"input": query.query})

    print("Output:", result["output"])

    return {
        "input": query.query,
        "output": result["output"]
    }
