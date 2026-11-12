import os
import time
from dotenv import load_dotenv
from groq import Groq

# Start the timer immediately
start_time = time.time()
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "openai/gpt-oss-120b"

# Define the multi-step math prompt
prompt = """
Solve the following business math problem step-by-step. 

Problem:
A SaaS product has 1200 users. 15% are on the Pro plan at ₹999/month. 
Calculate:
1. The number of Pro users.
2. The total monthly revenue.
3. The total annual revenue.
4. The new monthly revenue if the number of Pro users grows by 20%.

Instructions:
You MUST show your thoughts, formulas, and calculations for Step 1, Step 2, Step 3, and Step 4 explicitly before providing the final values.

Structure your final response exactly like this:
[Thinking & Calculations]
...
Final Summary:
- Current Pro Users: [Value]
- Monthly Revenue: [Value]
- Annual Revenue: [Value]
- New Monthly Revenue (20% Growth): [Value]
"""

print(f"Running Multi-Step Chain-of-Thought Math Problem using {MODEL_NAME}...\n")

try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0  # Keep math completely deterministic and accurate
    )
    
    # Print the direct terminal output
    print("="*20 + " CHAIN-OF-THOUGHT REASONING OUTPUT " + "="*20)
    print(response.choices[0].message.content.strip())
    print("="*75)

except Exception as e:
    print(f" Error occurred: {e}")

total_time = time.time() - start_time
print(f"Execution Completed in {total_time:.2f} seconds.\n")