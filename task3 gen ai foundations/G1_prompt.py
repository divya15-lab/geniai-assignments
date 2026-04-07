print("STARTING SCRIPT")
import ollama

print("===== G1: Prompt → JSON =====")

input_text = "Create a cylinder with height 10cm and radius 5cm"
print("\nInput:", input_text)

prompt = f"""
Convert the following text into JSON.

Return ONLY JSON:
{{"shape": "cylinder", "height": 10, "radius": 5}}

Text: {input_text}
"""

print("\nCalling LLM... please wait")

try:
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    # DEBUG: print full response
    print("\nFull Response:", response)

    output = response.get('message', {}).get('content', '')

    print("\nLLM Output:")
    print(output)

except Exception as e:
    print("\nERROR:", e)

print("\n===== Done =====")
