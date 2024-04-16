from pinecone import Pinecone
from dotenv import load_dotenv
import json
import os
import uuid
import argparse

load_dotenv()
API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "default_namespace")
DATA_FILE =  os.getenv("DATA_FILE", "data/search-data.jsonl")
PINECONE_INDEX_NAME = "search-ci"

def upsert_data():
    pc = Pinecone(api_key=API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    vectors = []

    with open(DATA_FILE, 'r') as f:
        data = [json.loads(line) for line in f]
    
    for entry in data:
        vector = {"id": str(uuid.uuid4()), 
                  "values": entry["embedding"],
                  "metadata": {"question": entry["question"], "answer": entry["answer"]}}
        vectors.append(vector)
    
    index.upsert(vectors=vectors, namespace=PINECONE_NAMESPACE)
    print(f"Upserted {len(vectors)} vectors in index: {PINECONE_INDEX_NAME} for namespace: {PINECONE_NAMESPACE}")

def delete_data():
    pc = Pinecone(api_key=API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    index.delete(delete_all=True, namespace=PINECONE_NAMESPACE)
    print(f"Deleted all vectors in index: {PINECONE_INDEX_NAME} for namespace: {PINECONE_NAMESPACE}")

def main():
    parser = argparse.ArgumentParser(description="CLI for upserting and deleted pinecone index data")
    parser.add_argument("action", choices=["upsert", "delete"], help="Action to perform: create or delete")
    args = parser.parse_args()

    if args.action == "upsert":
        upsert_data()
    elif args.action == "delete":
        delete_data()

if __name__ == "__main__":
    main()