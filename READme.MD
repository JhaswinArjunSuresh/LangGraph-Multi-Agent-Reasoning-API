# 🚀 Multi-Agent Reasoning API with LangGraph

This builds a multi-agent reasoning pipeline using 🧠 LangGraph + LangChain, exposed via FastAPI.

## Features
- Extractor (entities) -> Coder (Python fn) -> Verifier (check code)
- Saves trace in SQLite, accessible via `/history/{run_id}`.

## Run locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
uvicorn app.main:app --reload
```

## Run with Docker
```bash
docker build -t multi-agent-api .
docker run -e OPENAI_API_KEY=your_key_here -p 8000:8000 multi-agent-api
```

## Usage
```bash
curl -X POST "http://127.0.0.1:8000/run_graph" -H "Content-Type: application/json" -d '{"text": "Elon Musk founded SpaceX in 2002."}'
```

## Diagram
Client -> FastAPI -> LangGraph
  ├─ Extractor -> Coder -> Verifier
  -> SQLite trace
