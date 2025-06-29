from sqlmodel import SQLModel, Session, create_engine

engine = create_engine("sqlite:///./graph_traces.db")
session = Session(engine)

def init_db():
    SQLModel.metadata.create_all(engine)