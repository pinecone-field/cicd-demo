from sentence_transformers import SentenceTransformer
import json

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# CSV entry
entry = {
    "question": "What are the common data preprocessing steps?",
    "answer": "Common data preprocessing steps include cleaning data, transforming features, normalizing or scaling data, and splitting the data into training and testing sets."
}

# Generate the embedding for the question
embedding = model.encode([entry["question"]])

# Add the embedding to the entry
entry["embedding"] = embedding.tolist()

# Write the entry to a JSONL file
with open('data.jsonl', 'w') as f:
    f.write(json.dumps(entry) + '\n')