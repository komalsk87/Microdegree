import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# File Paths
TRAIN_FILE = 'customer_support_tickets_cleaned.csv'
TEST_FILE = 'test.csv'  # Replace with your test CSV filename

# =====================================================================
# CATEGORY 1: Custom ML Model (Trained on customer_support_tickets.csv)
# =====================================================================

print("--- Step 1: Loading Training Data & Building Category 1 ML Model ---")

# 1. Load Training Dataset
train_df = pd.read_csv(TRAIN_FILE)

# 2. Preprocess & Map Categories in Training Data
train_df['combined_text'] = (
    train_df['Ticket Subject'].fillna('') + " " + train_df['Ticket Description'].fillna('')
)

def map_category(ticket_type):
    tt = str(ticket_type).lower()
    if 'technical' in tt:
        return 'Technical'
    elif 'billing' in tt or 'refund' in tt or 'cancellation' in tt:
        return 'Billing'
    else:
        return 'Other'

train_df['Category'] = train_df['Ticket Type'].apply(map_category)

# 3. Build & Train ML Pipeline on Full Training File
ml_category_model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', MultinomialNB())
])

ml_category_model.fit(train_df['combined_text'], train_df['Category'])
print("ML Model training complete.")


# =====================================================================
# LOAD TEST CSV & PREDICT ON TEST DATA
# =====================================================================

print(f"\n--- Step 2: Loading Test File '{TEST_FILE}' & Making Predictions ---")

# Load Test Dataset
test_df = pd.read_csv(TEST_FILE)

# Combine text columns for the test data (adjust column names if different in your test CSV)
if 'Ticket Subject' in test_df.columns and 'Ticket Description' in test_df.columns:
    test_df['combined_text'] = (
        test_df['Ticket Subject'].fillna('') + " " + test_df['Ticket Description'].fillna('')
    )
elif 'Ticket Description' in test_df.columns:
    test_df['combined_text'] = test_df['Ticket Description'].fillna('')
else:
    # Fallback to the first text column available
    test_df['combined_text'] = test_df.iloc[:, 0].astype(str)

# Predict Category 1 using Trained ML Model
test_df['Predicted_Category'] = ml_category_model.predict(test_df['combined_text'])


# =====================================================================
# CATEGORY 2: Pre-Trained Sentiment Model (Downloaded from Net)
# =====================================================================

nltk.download('vader_lexicon', quiet=True)
sentiment_analyzer = SentimentIntensityAnalyzer()

def predict_sentiment_from_net(text):
    """Uses pre-trained VADER lexicon to infer customer sentiment."""
    scores = sentiment_analyzer.polarity_scores(str(text))
    compound = scores['compound']
    
    if compound <= -0.05:
        return 'angry'
    elif compound >= 0.05:
        return 'happy'
    else:
        return 'calm'

# Predict Sentiment using Category 2 Pre-trained Model
test_df['Predicted_Sentiment'] = test_df['combined_text'].apply(predict_sentiment_from_net)


# =====================================================================
# EVALUATION & SAVING RESULTS
# =====================================================================

# Optional: If your test CSV contains actual ground truth 'Ticket Type' column
if 'Ticket Type' in test_df.columns:
    test_df['Actual_Category'] = test_df['Ticket Type'].apply(map_category)
    print("\n--- Category 1 Model Evaluation on Test Dataset ---")
    print(classification_report(test_df['Actual_Category'], test_df['Predicted_Category']))

# Save predictions to a new output CSV file
test_df.to_csv('test_predictions_output.csv', index=False)
print("\nPredictions successfully saved to 'test_predictions_output.csv'!")

# Display preview of predictions on test set
print("\nFirst 5 Predicted Output Rows:")
print(test_df[['combined_text', 'Predicted_Category', 'Predicted_Sentiment']].head())

joblib.dump(ml_category_model, 'category_model.pkl')