import ollama

MODEL_NAME = "llama3.2"

# ==========================================
# 1. CORE PROMPTING STRATEGIES
# ==========================================

print("=== 1. Zero-Shot Prompting ===")
zero_shot = ollama.chat(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Classify the sentiment: 'The food was terrible.'"}]
)
print("Output:", zero_shot["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 2. Few-Shot Prompting ===")
few_shot = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": "Text: 'Love it!' -> Sentiment: Positive"},
        {"role": "user", "content": "Text: 'Broke instantly.' -> Sentiment: Negative"},
        {"role": "user", "content": "Text: 'The box is blue.' -> Sentiment: Neutral"},
        {"role": "user", "content": "Text: 'The service was slow.' -> Sentiment:"}
    ]
)
print("Output:", few_shot["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 3. Role Prompting ===")
role_prompt = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a 19th-century pirate captain."},
        {"role": "user", "content": "How do I fix a bug in my code?"}
    ]
)
print("Output:", role_prompt["message"]["content"])
print("\n" + "="*40 + "\n")


# ==========================================
# 2. ADVANCED REASONING & LOGIC TECHNIQUES
# ==========================================

print("=== 4. Chain-of-Thought (CoT) ===")
cot_prompt = ollama.chat(
    model=MODEL_NAME,
    messages=[{
        "role": "user", 
        "content": "I have 3 apples. I buy 2 more bags with 6 apples each. I eat 1 apple. "
                   "Think step-by-step before giving the final answer."
    }]
)
print("Output:", cot_prompt["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 5. Tree-of-Thoughts (ToT) ===")
tot_prompt = ollama.chat(
    model=MODEL_NAME,
    messages=[{
        "role": "user", 
        "content": "Generate 3 distinct strategies to increase website traffic for an online bakery. "
                   "Evaluate the pros and cons of each, then select the best one."
    }]
)
print("Output:", tot_prompt["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 6. Self-Consistency ===")
print("Running 3 separate inference passes...")
responses = []
for i in range(3):
    res = ollama.chat(
        model=MODEL_NAME,
        options={"temperature": 0.7},
        messages=[{"role": "user", "content": "A store has a 20% discount on a $50 shirt. What is the final price?"}]
    )
    responses.append(res["message"]["content"])
    print(f"--- Pass {i+1} Output ---")
    print(res["message"]["content"])
print("\n" + "="*40 + "\n")


# ==========================================
# 3. OUTPUT CONTROL & GUARDRAILS
# ==========================================

print("=== 7. Structured JSON Output ===")
json_prompt = ollama.chat(
    model=MODEL_NAME,
    format="json",
    messages=[{
        "role": "user", 
        "content": "Extract details into JSON with keys 'name', 'age', and 'profession': "
                   "'John Doe, 29 years old, software engineer.'"
    }]
)
print("Output:", json_prompt["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 8. Negative Constraints ===")
constraint_prompt = ollama.chat(
    model=MODEL_NAME,
    messages=[{
        "role": "user", 
        "content": "Summarize how solar panels work in 2 sentences. "
                   "Do NOT use technical jargon like 'photovoltaic' or 'semiconductors'."
    }]
)
print("Output:", constraint_prompt["message"]["content"])
print("\n" + "="*40 + "\n")


print("=== 9. Prompt Chaining ===")
# Step 1: Summarize
step1 = ollama.chat(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Summarize the key benefits of exercise."}]
)
summary = step1["message"]["content"]
print("Step 1 (Summary):")
print(summary)

print("\n----------------------------------------\n")

# Step 2: Translate output from Step 1
step2 = ollama.chat(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": f"Translate this summary to French:\n{summary}"}]
)
print("Step 2 (Translation):")
print(step2["message"]["content"])
print("\n" + "="*40 + "\n")