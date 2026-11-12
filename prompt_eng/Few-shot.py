import os
import time
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

# Start the timer immediately
start_time = time.time()
load_dotenv()

# Initialize the Groq cloud client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Using a highly efficient, fast open-source model hosted on Groq's cloud
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
Classify into exactly one category: Billing, Technical, Shipping. Return ONLY the word.
Examples:
Complaint: "My screen is frozen." -> Technical
Complaint: "I need a receipt." -> Billing
Complaint: "Where is my order?" -> Shipping
Complaint: "{complaint}" ->"""

predictions = []
print(f"Running Few-Shot via Groq API using {MODEL_NAME}...")

for text in complaints:
    try:
        # standard chat completion structure
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": get_prompt(text)}],
            temperature=0.0 # Keep it predictable
        )
        predictions.append(response.choices[0].message.content.strip().capitalize())
    except Exception as e:
        predictions.append(f"Error")
    
    # Tiny 1-second pause just as a coding best practice (Groq allows up to 30 requests per minute for free!)
    time.sleep(1.0)

total_time = time.time() - start_time

# Print Results Table
df = pd.DataFrame({"Complaint": complaints, "Few-Shot Classification": predictions})
pd.set_option('display.max_colwidth', None)

print("\n" + "="*20 + " GROQ API RESULTS " + "="*20)
print(df)
print("="*58)
print(f"Total Execution Time: {total_time:.2f} seconds\n")