from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)

try:
    completion = client.chat.completions.create(
        model = "qwen/qwen3.6-27b",
        messages = [
            {"role": "user",
             "content": "How do i do addition of two numbers in python?"}
        ]
    )

    print("Response from Groq API:")
    print(completion.choices[0].message.content)

except Exception as e:
    print("Error from Groq API:", str(e))