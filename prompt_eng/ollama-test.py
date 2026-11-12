import ollama

def start_local_chat(model_name: str = "llama3.2"):
    print(f"--- Local AI Chatbot ({model_name}) ---")
    print("Type 'exit' or 'quit' to end the session.\n")

    # Maintain conversation memory
    messages = [
        {
            "role": "system",
            "content": "You are a helpful, concise local AI assistant running entirely on the user's machine."
        }
    ]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Append user message to conversation history
        messages.append({"role": "user", "content": user_input})
        print(f"\n{model_name}: ", end="", flush=True)

        # Request a streaming response from Ollama
        stream = ollama.chat(
            model=model_name,
            messages=messages,
            stream=True
        )

        full_response = ""
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end="", flush=True)
            full_response += content

        print("\n")

        # Append assistant's response to history for context retention
        messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    start_local_chat()