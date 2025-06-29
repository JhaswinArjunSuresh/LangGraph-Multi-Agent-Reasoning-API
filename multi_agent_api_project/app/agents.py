from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

def extractor_agent(input_text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert NER extractor. Extract all named entities from the input."),
        ("human", f"Text: {input_text}")
    ])
    return llm(prompt.format_messages())

def coder_agent(task_description):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Python expert. Write a function as per instructions."),
        ("human", f"Instruction: {task_description}")
    ])
    return llm(prompt.format_messages())

def verifier_agent(code_snippet):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You verify Python code. Is it safe, does it match the task? Answer Yes or No with reason."),
        ("human", f"Code:\n{code_snippet}")
    ])
    return llm(prompt.format_messages())