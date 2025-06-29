from langgraph.graph import StateGraph
from .agents import extractor_agent, coder_agent, verifier_agent

def build_graph(input_text):
    g = StateGraph()
    
    def extract_node(state):
        entities_msg = extractor_agent(state['input'])
        state['entities'] = entities_msg.content
        return state

    def code_node(state):
        task_desc = f"write a function to process entities: {state['entities']}"
        code_msg = coder_agent(task_desc)
        state['code'] = code_msg.content
        return state

    def verify_node(state):
        verify_msg = verifier_agent(state['code'])
        state['verification'] = verify_msg.content
        return state

    g.add_node("extractor", extract_node)
    g.add_node("coder", code_node)
    g.add_node("verifier", verify_node)

    g.add_edge("extractor", "coder")
    g.add_edge("coder", "verifier")

    return g.compile()