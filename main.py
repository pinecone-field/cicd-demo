from typing import Union

from fastapi import FastAPI
from search.query import search_query
from recommendation.query import recommendation_query

app = FastAPI()

@app.post("/search")
def search(question: str):
    return {"answer": search_query(question)}

@app.post("/genai")
def genai(question: str):
    return None

@app.post("/recommend")
def recommend(query_text: str, 
              rsi_filter: float, 
              pe_filter: float, 
              dividend_filter: float):
    return {"recommendation": recommendation_query(query_text, rsi_filter, pe_filter, dividend_filter)}