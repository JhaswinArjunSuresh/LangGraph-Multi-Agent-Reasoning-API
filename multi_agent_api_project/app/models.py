from sqlmodel import SQLModel, Field
from typing import Optional
import json

class GraphTrace(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    run_id: str
    input_text: str
    output_data: str
    raw_trace: str

    def as_dict(self):
        return {
            "run_id": self.run_id,
            "input_text": self.input_text,
            "output_data": json.loads(self.output_data),
            "trace": json.loads(self.raw_trace),
        }