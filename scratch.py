import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sentence_transformers import SentenceTransformer

# Load the data
df = pd.read_json('./data/recommendation-data.jsonl', lines=True)

# Normalize numerical data
numerical_cols = ['rsi_rating', 'market_cap', 'dividend_yield', 'beta', 'pe', 'sma_rating', 'macd_rating']
min_max_scaler = MinMaxScaler()
scaled_numerical = min_max_scaler.fit_transform(df[numerical_cols])

text_cols = ['ticker','name','sector','industry','Headquarters Location']
model = SentenceTransformer('all-MiniLM-L6-v2')
text_embeddings = model.encode(df[text_cols].agg(' '.join, axis=1))


# Concatenate the processed categorical and numerical data
processed_data = pd.concat([pd.DataFrame(scaled_numerical), pd.DataFrame(text_embeddings)], axis=1)
embeddings = processed_data.values
print(embeddings[0].tolist())
print(len(embeddings[10]))