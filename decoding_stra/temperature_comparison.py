import sys
import time
import textwrap
import ollama

def run_factual_table_experiment():
    model_name = "llama3.2"
    prompt = "What is the capital of France? List three facts about it"
    
    # Verify local Ollama connection and model existence
    try:
        available_models = [m.model for m in ollama.list().models]
        if not any(model_name in m for m in available_models):
            print(f"[-] Error: Local model '{model_name}' not found.")
            print(f"Available local models: {available_models}")
            print(f"To pull this model, run in terminal: ollama pull {model_name}")
            sys.exit(1)
    except Exception as e:
        print(f"[-] Error connecting to local Ollama instance: {e}")
        print("Please ensure the Ollama desktop application or service is running.")
        sys.exit(1)

    runs = 5
    temp_0_results = []
    temp_1_results = []

    print("=" * 100)
    print("STARTING FACTUAL Q&A EXPERIMENT TO GENERATE DATA TABLE")
    print(f"Local Model: {model_name}")
    print(f"Prompt: '{prompt}'")
    print("=" * 100)

    # -------------------------------------------------------------
    # 1. Gather Temperature 0.0 Runs
    # -------------------------------------------------------------
    print("\n[+] Gathering 5 runs at Temperature 0.0 (Deterministic)...")
    for i in range(runs):
        print(f"    - Run {i+1}/{runs}...", end="", flush=True)
        try:
            response = ollama.chat(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                options={
                    "temperature": 0.0,
                    "num_predict": 150  # Equivalent to max_tokens
                }
            )
            content = response["message"]["content"].strip().replace("\n", " ")
            temp_0_results.append(content)
            print(" Done.")
        except Exception as e:
            print(f" Error: {e}")
            temp_0_results.append(f"Error fetching: {e}")
        time.sleep(0.5)

    # -------------------------------------------------------------
    # 2. Gather Temperature 1.0 Runs
    # -------------------------------------------------------------
    print("\n[+] Gathering 5 runs at Temperature 1.0 (Varied/Explorer)...")
    for i in range(runs):
        print(f"    - Run {i+1}/{runs}...", end="", flush=True)
        try:
            response = ollama.chat(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                options={
                    "temperature": 1.0,
                    "num_predict": 150
                }
            )
            content = response["message"]["content"].strip().replace("\n", " ")
            temp_1_results.append(content)
            print(" Done.")
        except Exception as e:
            print(f" Error: {e}")
            temp_1_results.append(f"Error fetching: {e}")
        time.sleep(0.5)

    # -------------------------------------------------------------
    # 3. Print Comparison Table
    # -------------------------------------------------------------
    print("\n" + "=" * 110)
    print("COMPARISON TABLE: TEMPERATURE 0.0 VS TEMPERATURE 1.0")
    print("=" * 110)

    # Column configuration widths
    col_run_w = 6
    col_t0_w = 48
    col_t1_w = 48

    # Table Header
    header_run = "Run #"
    header_t0 = "Temperature 0.0 (The Train on Tracks)"
    header_t1 = "Temperature 1.0 (The Free Explorer)"

    border_line = f"+{'-' * (col_run_w+2)}+{'-' * (col_t0_w+2)}+{'-' * (col_t1_w+2)}+"
    print(border_line)
    print(f"| {header_run:<{col_run_w}} | {header_t0:<{col_t0_w}} | {header_t1:<{col_t1_w}} |")
    print(border_line)

    for run_idx in range(runs):
        t0_text = temp_0_results[run_idx]
        t1_text = temp_1_results[run_idx]

        # Wrap text inside cell width limits
        t0_wrapped = textwrap.wrap(t0_text, width=col_t0_w)
        t1_wrapped = textwrap.wrap(t1_text, width=col_t1_w)

        # Handle rows with differing line counts
        max_lines = max(len(t0_wrapped), len(t1_wrapped))

        for line_idx in range(max_lines):
            run_label = f"Run {run_idx+1}" if line_idx == 0 else ""
            t0_line = t0_wrapped[line_idx] if line_idx < len(t0_wrapped) else ""
            t1_line = t1_wrapped[line_idx] if line_idx < len(t1_wrapped) else ""

            print(f"| {run_label:<{col_run_w}} | {t0_line:<{col_t0_w}} | {t1_line:<{col_t1_w}} |")
        
        print(border_line)

    print("\n[✔] Experiment completed successfully! Observe the near-identical output in Temp 0.0 vs word variation in Temp 1.0.")

if __name__ == "__main__":
    run_factual_table_experiment()
