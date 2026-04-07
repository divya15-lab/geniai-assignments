import ollama
import json

print("START")

def get_json_output(text):

    print("Inside function")

    prompt = f"""
    Convert this into JSON with keys: shape, height, radius.
    Return ONLY JSON.

    Text: {text}
    """

    print("Before LLM call")

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    print("After LLM call")

    output = response['message']['content']

    print("LLM Output:", output)

    try:
        parsed = json.loads(output)
        print("Parsed:", parsed)
        return parsed
    except Exception as e:
        print("Parsing error:", e)
        return None


input_text = "Create a cylinder with height 10cm and radius 5cm"

print("Calling function")

result = get_json_output(input_text)

print("Final result:", result)
