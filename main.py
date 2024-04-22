from fastapi import FastAPI
from question_answer.query import query as qa_query
from recommendation.query import query as rec_query

app = FastAPI()

@app.post("/question-answer")
def search(question: str):
    return {"answer": qa_query(question)}

@app.post("/recommendation")
def recommend(query_text: str, 
              rsi_filter: float, 
              pe_filter: float, 
              dividend_filter: float):
    return {"recommendation": rec_query(query_text, rsi_filter, pe_filter, dividend_filter)}