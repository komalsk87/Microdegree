import os
import time
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

# Start the timer immediately
start_time = time.time()
load_dotenv()

# Initialize Groq client
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
Classify the following customer complaint into exactly one of these categories: Billing, Technical, or Shipping. 
Return ONLY the single word category name. Do not include any punctuation, conversational text, or explanation.

Complaint: "{complaint}"
Category:"""

predictions = []
print("Running Zero-Shot Classification via Groq API...")

for text in complaints:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": get_prompt(text)}],
            temperature=0.0
        )
        predictions.append(response.choices[0].message.content.strip().capitalize())
    except Exception as e:
        print(f"Error processing complaint: {e}")
        predictions.append("Error")
    
    time.sleep(1.0) # Light pacing

total_time = time.time() - start_time

df = pd.DataFrame({"Complaint": complaints, "Zero-Shot Classification": predictions})
pd.set_option('display.max_colwidth', None)

print("\n" + "="*20 + " GROQ ZERO-SHOT RESULTS " + "="*20)
print(df)
print("="*64)
print(f"Total Execution Time: {total_time:.2f} seconds\n")
