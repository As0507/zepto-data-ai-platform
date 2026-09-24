from typing import TypedDict
from langgraph.graph import StateGraph

class State(TypedDict):
    query: str
    intent: str
    answer: str
    sources: list
    confidence: float

def classify_intent(state: State) -> State:
    q = state["query"].lower()
    keywords = ["delivery","return","refund","membership","tracking","cancel","gift card","support hours"]
    state["intent"] = "policy_question" if any(k in q for k in keywords) else "general_question"
    return state

def retrieve_and_answer(state: State) -> State:
    if state["intent"]=="policy_question":
        state["answer"]="Policy answer (mock)"
        state["sources"]=["doc_01"]
        state["confidence"]=1.0
    else:
        state["answer"]="General answer (mock)"
        state["sources"]=[]
        state["confidence"]=1.0
    return state

graph = StateGraph(State)
graph.add_node("classify_intent", classify_intent)
graph.add_node("retrieve_and_answer", retrieve_and_answer)
graph.set_entry_point("classify_intent")
graph.add_edge("classify_intent","retrieve_and_answer")
