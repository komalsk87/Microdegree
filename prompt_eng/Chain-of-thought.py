import os
import time
import re
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

start_time = time.time()
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "openai/gpt-oss-120b"

complaints = [
    "I was charged twice for my subscription this month. Please refund.",
    "The app keeps crashing every time I try to open the camera roll.",
    "My package was supposed to arrive yesterday but tracking says it's delayed.",
    "I cannot log into my account, it says password incorrect but I reset it.",
    "There is an unknown $45 fee on my latest invoice. What is this?",
    "The box arrived completely damaged and the item inside is broken.",
    "Can I change my delivery address to my office instead of my home?",
    "The website is throwing a 500 internal server error during checkout.",
    "I applied a 20% discount code but it didn't apply to my final total.",
    "The courier left my parcel in the rain and now it is ruined."
]

def get_prompt(complaint):
    return f"""
Classify this complaint into Billing, Technical, or Shipping. Think step-by-step.
At the very end of your response, write "Final Category: " followed by the isolated category name.
Complaint: "{complaint}"
Thinking Process:"""

predictions = []
print(f"Running Chain-of-Thought Classification via Groq API...")

for text in complaints:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": get_prompt(text)}],
            temperature=0.0
        )
        full_text = response.choices[0].message.content.strip()
        
        # Regex extraction to strip the thinking process and grab just the final label for the table
        match = re.search(r"Final Category:\s*(\w+)", full_text, re.IGNORECASE)
        if match:
            predictions.append(match.group(1).strip().capitalize())
        else:
            # Fallback text check if it ignores the structural instruction format
            if "Billing" in full_text: predictions.append("Billing")
            elif "Technical" in full_text: predictions.append("Technical")
            elif "Shipping" in full_text: predictions.append("Shipping")
            else: predictions.append("Unknown")
    except Exception:
        predictions.append("Error")
    
    time.sleep(1.0)

total_time = time.time() - start_time

df = pd.DataFrame({"Complaint": complaints, "CoT Classification": predictions})
pd.set_option('display.max_colwidth', None)

print("\n" + "="*20 + " GROQ CHAIN-OF-THOUGHT RESULTS " + "="*20)
print(df)
print("="*71)
print(f"Total Execution Time: {total_time:.2f} seconds\n")