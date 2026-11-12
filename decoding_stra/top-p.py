import random

def print_raw_vocabulary(vocabulary):
    """
    Displays the entire vocabulary pool of candidate tokens with their raw,
    unfiltered probabilities before any Top-p sampling takes place.
    """
    sorted_vocab = sorted(vocabulary.items(), key=lambda item: item[1], reverse=True)
    print("=" * 70)
    print("ALL PREDICTABLE TOKENS & RAW PROBABILITIES (Before Top-p Filtering)")
    print("=" * 70)
    for word, prob in sorted_vocab:
        print(f"  - {word.upper():<15} : {prob * 100:>5.1f}%")
    print("=" * 70 + "\n")

def simulate_top_p(prompt, vocabulary, top_p_value):
    """
    Simulates Top-p (Nucleus) Sampling showing only the allowed next tokens
    and the resulting generated sentence, without the step-by-step math.
    """
    # Sort vocabulary descending by probability
    sorted_vocab = sorted(vocabulary.items(), key=lambda item: item[1], reverse=True)
    
    # Identify which tokens make it into the nucleus pool
    allowed_tokens = []
    cumulative_sum = 0.0
    
    for word, prob in sorted_vocab:
        allowed_tokens.append(word.upper())
        cumulative_sum += prob
        if cumulative_sum >= top_p_value:
            break
            
    # Normalize probabilities of allowed tokens for a mathematically correct selection
    total_allowed_prob = sum(vocabulary[word.lower()] for word in allowed_tokens)
    normalized_weights = [vocabulary[word.lower()] / total_allowed_prob for word in allowed_tokens]
    chosen_token = random.choices(allowed_tokens, weights=normalized_weights, k=1)[0]
    
    # Display the clean output
    print("=" * 70)
    print(f"Base Sentence:       \"{prompt}...\"")
    print(f"Top-p Value:         {top_p_value}")
    print(f"Allowed Next Tokens: {', '.join(allowed_tokens)}")
    print(f"Generated Output:    \"{prompt} {chosen_token}\"")
    
    # Explain the behavioral difference
    if top_p_value <= 0.3:
        print("Behavior Profile:    Highly deterministic. Restricts output strictly to the single highest-probability token.")
    elif top_p_value <= 0.5:
        print("Behavior Profile:    Locked into highly predictable, safe, and conventional outcomes.")
    elif top_p_value <= 0.9:
        print("Behavior Profile:    Allowed to explore creative, metaphorical, and diverse paths.")
    else:
        print("Behavior Profile:    Unrestricted exploration. The entire vocabulary is allowed, including low-probability noise.")
    print("=" * 70 + "\n")

# ---- Run the Demonstration ----
if __name__ == "__main__":
    robot_vocabulary = {
        "eyes": 0.20,
        "chest": 0.30,
        "hatch": 0.15,
        "mind": 0.10,
        "banana": 0.049,
        "refrigerator": 0.001
    }
    
    partial_prompt = "The door of the robot opened, revealing its"
    
    # Step 1: Print the raw candidates before filtering
    print_raw_vocabulary(robot_vocabulary)
    
    # Step 2: Simulate predictions across the specified Top-p thresholds
    for p_value in [0.3, 0.5, 0.9, 1.0]:
        simulate_top_p(partial_prompt, robot_vocabulary, top_p_value=p_value)