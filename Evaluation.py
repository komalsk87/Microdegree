import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load the generated predictions output CSV file
FILE_PATH = 'test_predictions_output.csv'
df = pd.read_csv(FILE_PATH)

# 2. Map original ticket types to standard target categories (Technical, Billing, Other)
def map_category(ticket_type):
    tt = str(ticket_type).lower()
    if 'technical' in tt:
        return 'Technical'
    elif 'billing' in tt or 'refund' in tt or 'cancellation' in tt:
        return 'Billing'
    else:
        return 'Other'

# Ensure ground truth category column exists
if 'Ticket Type' in df.columns:
    df['Actual_Category'] = df['Ticket Type'].apply(map_category)
elif 'Actual_Category' not in df.columns:
    raise KeyError(
        "Ground truth category column ('Ticket Type' or 'Actual_Category') not found in CSV."
    )

# 3. Create a comparison column to check if prediction is right or wrong
df['Is_Correct'] = df['Actual_Category'] == df['Predicted_Category']

# 4. Calculate Overall Accuracy
accuracy = accuracy_score(df['Actual_Category'], df['Predicted_Category'])

# ---------------------------------------------------------------------
# DISPLAY EVALUATION RESULTS
# ---------------------------------------------------------------------

print("=" * 60)
print(f" CATEGORY 1 MODEL ACCURACY: {accuracy * 100:.2f}%")
print("=" * 60)

# Display sample row-by-row comparisons (Right vs. Wrong)
print("\n--- Row-by-Row Prediction Check (First 10 Rows) ---")
print(
    df[['combined_text', 'Actual_Category', 'Predicted_Category', 'Is_Correct']].head(10)
)

# Display correctness summary counts
print("\n--- Prediction Summary Counts ---")
print(df['Is_Correct'].value_counts().rename({True: 'Correct', False: 'Incorrect'}))

# Display Detailed Classification Metrics (Precision, Recall, F1-Score)
print("\n--- Classification Report ---")
print(classification_report(df['Actual_Category'], df['Predicted_Category']))

# Display Confusion Matrix
print("--- Confusion Matrix ---")
cm = pd.crosstab(
    df['Actual_Category'],
    df['Predicted_Category'],
    rownames=['Actual'],
    colnames=['Predicted']
)
print(cm)