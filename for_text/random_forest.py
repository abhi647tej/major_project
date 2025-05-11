# train_suspicious_chat_model.py

import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("english_dataset.csv")

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text.strip()

# Apply preprocessing
df['Clean_Chat'] = df['Chat'].apply(preprocess_text)

# Define pipeline: TF-IDF + Random Forest
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=500, ngram_range=(1, 2))),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df['Clean_Chat'], df['Label'], test_size=0.2, random_state=42)

# Fit model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(pipeline, "suspicious_chat_rf_model.pkl")
print("✅ Model saved as suspicious_chat_rf_model.pkl")
