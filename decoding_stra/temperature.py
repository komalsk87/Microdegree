import sys
import time
import ollama

def run_experiment():
    # Model configuration - adjust to any local model you have pulled (e.g., llama3.2, mistral, gemma2)
    model_name = "llama3.2" 
    
    # Verify Ollama local connection and model availability
    try:
        available_models = [m.model for m in ollama.list().models]
        if not any(model_name in m for m in available_models):
            print(f"[-] Error: Local model '{model_name}' not found.")
            print(f"Available local models: {available_models}")
            print(f"To pull this model, run: ollama pull {model_name}")
            sys.exit(1)
    except Exception as e:
        print(f"[-] Error connecting to local Ollama instance: {e}")
        print("Please ensure the Ollama desktop app or service is running.")
        sys.exit(1)

    prompt = "Write a story on mickey mouse"
    temperatures = [0.0, 0.5, 1.0, 1.5]

    print("=" * 60, flush=True)
    print(f"Starting Temperature Experiment using local model: {model_name}", flush=True)
    print(f"Prompt: '{prompt}'", flush=True)
    print("=" * 60, flush=True)

    for temp in temperatures:
        print(f"\n Running Local Inference with Temperature: {temp}...", flush=True)
        
        try:
            # Ollama accepts hyperparameter options via the 'options' dict
            response = ollama.chat(
                model=model_name,
                messages=[
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                options={
                    "temperature": temp,
                    "num_predict": 70  # Equivalent to max_tokens in API specs
                }
            )
            
            content = response["message"]["content"].strip()
            
            # Print directly to the terminal
            print("-" * 40, flush=True)
            print(f"Results for Temperature {temp}:", flush=True)
            print(content, flush=True)
            print("-" * 40, flush=True)
            
        except Exception as e:
            print(f"[-] Local Error at temperature {temp}: {e}", flush=True)
        
        # Slight pause between local inference runs
        time.sleep(0.5)

    print("\n" + "=" * 60, flush=True)

if __name__ == "__main__":
    run_experiment()