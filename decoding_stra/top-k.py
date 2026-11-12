import numpy as np

def get_top_k_words(words, logits, k):
    """
    Selects and returns strictly the top k words based on highest logit scores.
    """
    # 1. Get indices sorted by logit values in descending order
    sorted_indices = np.argsort(logits)[::-1]
    
    # 2. Pick only the top k indices
    top_k_indices = sorted_indices[:k]
    
    # 3. Retrieve the corresponding words
    chosen_words = [words[i] for i in top_k_indices]
    
    return chosen_words

# --- Data Setup ---
words = ["cat", "dog", "car", "banana", "galaxy"]
logits = np.array([5.0, 4.5, 2.0, 0.1, -1.0])

# --- Test with different Top-k values ---

print("=== ALL WORDS & SCORES ===")
for word, score in zip(words, logits):
    print(f"{word}: {score}")

print("\n==========================")

# Example 1: Top-k = 2
k = 2
top_2_words = get_top_k_words(words, logits, k)
print(f"Top-k = {k} Chosen Words:", top_2_words)

# Example 2: Top-k = 4
k = 3
top_3_words = get_top_k_words(words, logits, k)
print(f"Top-k = {k} Chosen Words:", top_3_words)