# Support Assistant

## Steps
1. Corpus: 8 policy docs in `/docs`.
2. Embeddings: generated locally with `sentence-transformers` + stored in ChromaDB.
3. LangGraph: nodes → `classify_intent`, `retrieve_and_answer`.
4. FastAPI: `/ask` endpoint returns JSON {answer, sources, confidence}.
5. Dockerfile: builds and runs locally with `uvicorn`.

## Example Calls
```bash
curl -X POST http://127.0.0.1:7860/ask -H "Content-Type: application/json" -d '{"query":"What is Zepto delivery policy?"}'
