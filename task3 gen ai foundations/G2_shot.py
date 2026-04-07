import ollama

print("===== G2: Zero-shot vs Few-shot =====")

# -------------------------
# Zero-shot Prompt
# -------------------------
zero_prompt = """
Convert this into JSON.

Text: Create a cylinder with height 10cm and radius 5cm

Return only JSON.
"""

print("\nRunning Zero-shot...")

response1 = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': zero_prompt}]
)

print("\nZero-shot Output:")
print(response1['message']['content'])

# -------------------------
# Few-shot Prompt
# -------------------------
few_prompt = """
Example:
Input: Create a cube of size 5cm
Output: {"shape":"cube","size":5}

Now convert this:

Input: Create a cylinder with height 10cm and radius 5cm

Return only JSON.
"""

print("\nRunning Few-shot...")

response2 = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': few_prompt}]
)

print("\nFew-shot Output:")
print(response2['message']['content'])

print("\n===== G2 Completed =====")
