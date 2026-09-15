import io
import pandas as pd
import joblib
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI(title="CSV Batch Ticket Classifier")

# Load trained Category 1 ML Model and Pre-trained Sentiment Model
category_model = joblib.load('category_model.pkl')
nltk.download('vader_lexicon', quiet=True)
sentiment_analyzer = SentimentIntensityAnalyzer()

def predict_sentiment(text):
    scores = sentiment_analyzer.polarity_scores(str(text))
    compound = scores['compound']
    if compound <= -0.05:
        return 'angry'
    elif compound >= 0.05:
        return 'happy'
    else:
        return 'calm'

# 1. Render Web Page with CSV File Upload Form
@app.get("/", response_class=HTMLResponse)
def serve_upload_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Batch CSV Classifier</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 60px auto; padding: 20px; text-align: center; }
            .card { border: 2px dashed #007bff; padding: 40px; border-radius: 10px; background: #f8f9fa; }
            input[type="file"] { margin: 20px 0; font-size: 14px; }
            button { background-color: #007bff; color: white; border: none; padding: 12px 24px; font-size: 16px; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <h2>Customer Support CSV Batch Classifier</h2>
        <div class="card">
            <form action="/predict-csv" method="post" enctype="multipart/form-data">
                <p>Select your CSV test file to process predictions:</p>
                <input type="file" name="file" accept=".csv" required><br>
                <button type="submit">Upload & Download Classified CSV</button>
            </form>
        </div>
    </body>
    </html>
    """

# 2. Endpoint to Process CSV & Return Download File
@app.post("/predict-csv")
async def process_and_download_csv(file: UploadFile = File(...)):
    # Read the uploaded CSV file
    df = pd.read_csv(file.file)
    
    # Process input text
    if 'Ticket Subject' in df.columns and 'Ticket Description' in df.columns:
        df['combined_text'] = df['Ticket Subject'].fillna('') + " " + df['Ticket Description'].fillna('')
    elif 'Ticket Description' in df.columns:
        df['combined_text'] = df['Ticket Description'].fillna('')
    else:
        df['combined_text'] = df.iloc[:, 0].astype(str)
        
    # Generate Category 1 ML Predictions & Category 2 Sentiment Predictions
    df['Predicted_Category'] = category_model.predict(df['combined_text'])
    df['Predicted_Sentiment'] = df['combined_text'].apply(predict_sentiment)
    
    # Clean up temporary combined text column if created separately
    if 'Ticket Subject' in df.columns and 'Ticket Description' in df.columns:
        df.drop(columns=['combined_text'], inplace=True)
        
    # Convert DataFrame to in-memory CSV stream
    output_stream = io.StringIO()
    df.to_csv(output_stream, index=False)
    
    # Return as an automatic downloadable file attachment
    response = StreamingResponse(
        iter([output_stream.getvalue()]),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = f"attachment; filename=predicted_{file.filename}"
    return response