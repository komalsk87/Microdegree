import time
import requests

url = "http://localhost:11434/api/chat"
models = ["llama3.2", "mistral"]
prompt = "Explain quantum computing in two simple sentences for a high school student."

for model in models:
    print("Testing model:", model)
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    start_time = time.time()
    response = requests.post(url, json=data)
    end_time = time.time()

    latency = end_time - start_time
    result = response.json()

    # Check if Ollama returned an error
    if "error" in result:
        print("Error from Ollama:", result["error"])
    else:
        answer = result["message"]["content"]
        print("Time taken:", round(latency, 2), "seconds")
        print("Answer:")
        print(answer)
        
    print("-" * 40)