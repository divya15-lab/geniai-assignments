from langgraph.graph import StateGraph
from typing import TypedDict
import ollama

print("===== LG2: Conditional Graph =====")

# -------------------------------
# State
# -------------------------------
class State(TypedDict):
    input: str
    summary: str
    output: str

# -------------------------------
# Node 1: Decision
# -------------------------------
def check_length(state):
    text = state["input"]

    if len(text) > 80:
        return "summarize"
    else:
        return "direct"

# -------------------------------
# Node 2: Summarize
# -------------------------------
def summarize_node(state):
    text = state["input"]

    prompt = f"Summarize this text in one line:\n{text}"

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    summary = response['message']['content']

    return {"summary": summary}

# -------------------------------
# Node 3: Direct return
# -------------------------------
def direct_node(state):
    return {"output": state["input"]}

# -------------------------------
# Node 4: Output
# -------------------------------
def output_node(state):
    if "output" in state:
        return {"output": state["output"]}
    else:
        return {"output": state["summary"]}

# -------------------------------
# Build Graph
# -------------------------------
graph = StateGraph(State)

graph.add_node("summarize", summarize_node)
graph.add_node("direct", direct_node)
graph.add_node("output", output_node)

# Conditional edge
graph.set_entry_point("summarize")  # temporary

graph.add_conditional_edges(
    "__start__",   # entry point
    check_length,
    {
        "summarize": "summarize",
        "direct": "direct"
    }
)

graph.add_edge("summarize", "output")
graph.add_edge("direct", "output")

app = graph.compile()

# -------------------------------
# Test
# -------------------------------
input_text = "Artificial Intelligence is transforming the way we interact with technology by enabling machines to learn from data and make intelligent decisions. Modern AI systems use machine learning and deep learning techniques to process large amounts of data, recognize patterns, and provide meaningful outputs. This has applications in healthcare, finance, education, and many other industries."

# Try long text also to test
# input_text = "Long paragraph..."

result = app.invoke({"input": input_text})

print("\nFinal Output:")
print(result["output"])

print("\n===== LG2 Completed =====")
