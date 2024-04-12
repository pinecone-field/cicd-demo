from pinecone import Pinecone, ServerlessSpec, PineconeApiException
from dotenv import load_dotenv
import os
import sys
import argparse

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")
INDEXES = ["search-ci", "recommendation-ci", "genai-ci"]
DIMENSIONS = 384
METRIC = "cosine"

def create_indexes():
    pc = Pinecone(api_key=API_KEY)
    for index in INDEXES:
        try:
            pc.create_index(name=index, dimension=DIMENSIONS, metric=METRIC,
            spec=ServerlessSpec(
                cloud="aws",
                region="us-west-2"
            ))
            print(f"Pinecone control plane: {index} index created successfully")
        except PineconeApiException as pae:
            print("Pinecone control plane API exception: Please check the error message below:")
            print(pae)
            sys.exit(1)

def delete_indexes():
    pc = Pinecone(api_key=API_KEY)
    for index in INDEXES:
        try:
            pc.delete_index(name=index)
            print(f"Pinecone control plane: {index} index deleted successfully")
        except PineconeApiException as pae:
            print("Pinecone control plane API exception: Please check the error message below:")
            print(pae)
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CLI for creating and deleting Pinecone indexes")
    parser.add_argument("action", choices=["create", "delete"], help="Action to perform: create or delete")
    args = parser.parse_args()

    if args.action == "create":
        create_indexes()
    elif args.action == "delete":
        delete_indexes()

if __name__ == "__main__":
    main()