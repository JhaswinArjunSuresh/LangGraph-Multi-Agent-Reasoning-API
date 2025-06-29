from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .db import init_db, session
from .models import GraphTrace
from .graph import build_graph
import uuid
import json

app = FastAPI()

class InputRequest(BaseModel):
    text: str

@app.on_event("startup")
def startup_event():
    init_db()

@app.post("/run_graph")
def run_graph(input_req: InputRequest):
    run_id = str(uuid.uuid4())
    input_text = input_req.text
    compiled_graph = build_graph(input_text)
    
    initial_state = {'input': input_text}
    final_state = compiled_graph.invoke(initial_state)

    trace = GraphTrace(
        run_id=run_id,
        input_text=input_text,
        output_data=json.dumps(final_state),
        raw_trace=json.dumps(compiled_graph.get_debug_trace())
    )
    session.add(trace)
    session.commit()
    return {"run_id": run_id, "result": final_state}

@app.get("/history/{run_id}")
def get_history(run_id: str):
    trace = session.query(GraphTrace).filter(GraphTrace.run_id == run_id).first()
    if not trace:
        raise HTTPException(status_code=404, detail="Not found")
    return trace.as_dict()