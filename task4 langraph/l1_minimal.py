from langgraph.graph import StateGraph
from typing import TypedDict
import ollama

print("===== LG1: Minimal Graph =====")

# ✅ Proper State
class State(TypedDict):
    input: str
    summary: str
    output: str

# Node 1
def summarize_node(state):
    text = state["input"]

    prompt = f"Summarize this text in one line:\n{text}"

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    summary = response['message']['content']

    return {"summary": summary}

# Node 2
def output_node(state):
    return {"output": state["summary"]}

# Build graph
graph = StateGraph(State)

graph.add_node("summarize", summarize_node)
graph.add_node("output", output_node)

graph.set_entry_point("summarize")
graph.add_edge("summarize", "output")

app = graph.compile()

# Run
input_text = "LangChain is a framework used to build applications powered by large language models."

result = app.invoke({"input": input_text})

print("\nFinal Output:")
print(result["output"])
