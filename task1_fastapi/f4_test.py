# f4_test.py
import requests

BASE = "http://127.0.0.1:8000"

# Test /ping
response = requests.get(f"{BASE}/ping")
print("Ping:", response.json())

# Test /greet
response = requests.get(f"{BASE}/greet", params={"name": "Divya"})
print("Greet:", response.json())

# Test /summarize
response = requests.post(f"{BASE}/summarize", json={"text": "This is a test"})
print("Summarize:", response.json())
