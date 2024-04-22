# query.py
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_RECOMMENDATION")

def generate_embedding(query_text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(query_text)

    return embedding.tolist()

def query(query_text, rsi_filter, pe_filter, dividend_filter):
    try:
        embedding = generate_embedding(query_text)
        pc = Pinecone(api_key=PINECONE_API_KEY)
        index = pc.Index(PINECONE_INDEX_NAME)

        result = index.query(
            namespace=PINECONE_NAMESPACE,
            vector=embedding,
            top_k=3,
            filter={
                    "RSI": {"$lte": rsi_filter},
                    "Dividend Yield": {"$gte": dividend_filter},
                    "PE": {"$lte": pe_filter}
                    },
            include_metadata=True
        )
        print(f"Query is for: {PINECONE_INDEX_NAME} index in the {PINECONE_NAMESPACE} namespace")

        # if result.matches[0].score < 0.5:
        #     return "Sorry, I do not have a recommendation for you."
        
        for r in result.matches:
            recommendation = r.metadata["ticker"]
            score = r.score
            print(f"Query Text: {query_text} \nRecommendation: {recommendation} \nSimilarity score: {score}")
        
        return result.matches
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e