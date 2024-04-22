from pinecone import Pinecone
from dotenv import load_dotenv
import json
import os
import uuid
import argparse
from sentence_transformers import SentenceTransformer

load_dotenv()
API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_RECOMMENDATION")
SOURCE_DATA_FILE =  os.getenv("SOURCE_DATA_FILE", "data/recommendation-data.jsonl")
DATA_FILE = os.getenv("DATA_FILE", "data/recommendation-data-with-embeddings.jsonl")

def upsert_data():
    pc = Pinecone(api_key=API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    vectors = []

    with open(DATA_FILE, 'r') as f:
        data = [json.loads(line) for line in f]
    
    for entry in data:
        vector = {"id": str(uuid.uuid4()), 
                  "values": entry["embedding"],
                  "metadata": {"ticker": entry["ticker"], 
                               "name": entry["name"], 
                               "sector": entry["sector"], 
                               "industry": entry["industry"],
                               "Headquarters Location": entry["Headquarters Location"],
                               "Date": entry["Date added"],
                               "Founded": entry["Founded"],
                               "RSI": entry["rsi_rating"],
                               "SMA Rating": entry["sma_rating"],
                               "MACD Rating": entry["macd_rating"],
                               "Market Cap": entry["market_cap"],
                               "Dividend Yield": entry["dividend_yield"],
                               "Beta": entry["beta"],
                               "PE": entry["pe"]}}
        vectors.append(vector)
    
    index.upsert(vectors=vectors, namespace=PINECONE_NAMESPACE)
    print(f"Upserted {len(vectors)} vectors in index: {PINECONE_INDEX_NAME} for namespace: {PINECONE_NAMESPACE}")

def delete_data():
    pc = Pinecone(api_key=API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    index.delete(delete_all=True, namespace=PINECONE_NAMESPACE)
    print(f"Deleted all vectors in index: {PINECONE_INDEX_NAME} for namespace: {PINECONE_NAMESPACE}")

def generate_embeddings():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    entries = []
    with open(SOURCE_DATA_FILE, 'r') as f:
        for line in f:
            entry = json.loads(line)
            text_columns = (
                f"ticker: {entry['ticker']} "
                f"name: {entry['name']} "
                f"sector: {entry['sector']} "
                f"industry: {entry['industry']} "
                f"headquarters: {entry['Headquarters Location']} "
            )

            entry["embedding"] = model.encode(text_columns).tolist()
            entries.append(entry)
            print(f"Generated embedding for record: {entry['ticker']}")
    
    with open(DATA_FILE, 'w') as f1:
        for entry in entries:
            f1.write(json.dumps(entry) + '\n')
        print(f"Generated new data file for {len(entries)} entries: {DATA_FILE}")

def main():
    parser = argparse.ArgumentParser(description="CLI for upserting and deleted pinecone index data")
    parser.add_argument("action", choices=["upsert", "delete", "gen"], help="Action to perform: create or delete or generate embeddings")
    args = parser.parse_args()

    if args.action == "upsert":
        upsert_data()
    elif args.action == "delete":
        delete_data()
    elif args.action == "gen":
        generate_embeddings()

if __name__ == "__main__":
    main()