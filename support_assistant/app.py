from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from graph import graph

class Query(BaseModel):
    query: str

class Response(BaseModel):
    answer: str
    sources: list
    confidence: float

app = FastAPI()

@app.post("/ask", response_model=Response)
def ask(q: Query):
    state={"query":q.query}
    result=graph.run(state)
    return Response(answer=result["answer"],sources=result["sources"],confidence=result["confidence"])

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=7860)
