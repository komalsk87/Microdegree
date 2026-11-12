import sys
import os
import time
from dotenv import load_dotenv
from groq import Groq

# Start tracking execution time
start_time = time.time()
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "openai/gpt-oss-120b"

# ==========================================
# COMMAND-LINE FILE HANDLING
# ==========================================
# Check if the user forgot to provide the text file path
if len(sys.argv) < 2:
    print("\n Error: Missing text file path!")
    print("Usage format: python prompt_chain.py <path_to_file.txt>")
    print("Example:      python prompt_chain.py jd.txt\n")
    sys.exit(1)

file_path = sys.argv[1]

print("="*60)
print(f" Reading Job Description from file: {file_path}")
print("="*60)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        job_description = f.read().strip()
except FileNotFoundError:
    print(f"❌ Error: The file '{file_path}' could not be found.")
    print("Please check the filename and ensure it is in your current directory.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error reading file: {e}")
    sys.exit(1)

if not job_description:
    print("❌ Error: The text file is empty. Exiting.")
    sys.exit(1)

print(f"Successfully loaded {len(job_description)} characters of text.")

# ==========================================
# PROMPT PIPELINE DEFINITIONS
# ==========================================
prompt_1 = f"""
Analyze the job description text below and extract key hiring entities. 
Provide the output in a clean bulleted format with exactly three headers: Role Name, Required Skills, and Required Experience.

Job Content:
\"\"\"{job_description}\"\"\"
"""

def get_prompt_2(extracted_entities):
    return f"""
You are an ambitious job applicant. Use the extracted job entities provided below to write a tailored, compelling, 3-sentence introduction paragraph for a cover letter. Make it professional and direct.

Extracted Job Entities:
{extracted_entities}

Cover Letter Paragraph:
"""

# ==========================================
# EXECUTE PROMPT CHAIN
# ==========================================
print(f"\n Starting Prompt Chain using {MODEL_NAME}...\n")

try:
    # --- CALL 1: Extract Entities ---
    print(" Executing Call 1: Processing text file content...")
    response_1 = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt_1}],
        temperature=0.1
    )
    extracted_data = response_1.choices[0].message.content.strip()
    
    print("\n--- [Output from Call 1: Extracted Entities] ---")
    print(extracted_data)
    print("-" * 47 + "\n")
    
    time.sleep(1.0) # Light pacing pause
    
    # --- CALL 2: Generate Cover Letter ---
    print(" Executing Call 2: Engineering tailored introduction...")
    response_2 = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": get_prompt_2(extracted_data)}],
        temperature=0.7 
    )
    final_cover_letter = response_2.choices[0].message.content.strip()
    
    print("\n--- [Output from Call 2: Tailored Cover Letter] ---")
    print(final_cover_letter)
    print("-" * 50 + "\n")

except Exception as e:
    print(f"❌ Error during chain execution: {e}")

total_time = time.time() - start_time
print(f"Prompt Chain Completed Successfully in {total_time:.2f} seconds.\n")