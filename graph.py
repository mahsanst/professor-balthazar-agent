# Imports (add to her consultation_agent.py or separate)
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import TypedDict, Annotated, Sequence
import operator

# Her Tools (copy from consultation_agent.py)
# ... (save_user_context, creative_reframe, etc.)

# New Tools for Your Twist (Emotional Rephrasing)
@tool
def generate_steps(problem: str) -> list:
    """Breaks problem into empathetic steps."""
    prompt = f"Break '{problem}' into 3-5 positive steps."
    response = llm.invoke(prompt).content  # Her llm
    return [line.strip() for line in response.split("\n")][:5]

@tool
def rephrase_emotionally(text: str) -> str:
    """Rephrases angry/frustrated text politely."""
    prompt = f"Rephrase this emotional text kindly: '{text}'."
    return llm.invoke(prompt).content

# State (Shared Memory—Enhance Her Sessions)
class BaltazarState(TypedDict):
    messages: Annotated[Sequence[HumanMessage], operator.add]
    context: dict  # Her user_context_tracker output
    steps: list
    rephrased: str
    next: str

# Agents (Build on Her LlmAgent)
supervisor_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Baltazar: Route to Reframer (anger), Stepper (plans), or Validator."),
    MessagesPlaceholder("messages")
])
supervisor = supervisor_prompt | llm  # Her llm

# ... (Similar for Stepper/Rephraser/Validator using her tools + new ones)

# Graph Nodes (Handoffs)
def supervisor_node(state):
    msg = supervisor.invoke(state["messages"])
    route = "rephraser" if "angry" in msg.content.lower() else "stepper"
    return {"messages": [msg], "next": route}

# Build \& Compile
workflow = StateGraph(BaltazarState)
# Add nodes/edges...
app = workflow.compile()

print("✅ Multi-Agent Graph Ready—Test: app.invoke({'messages': [HumanMessage('Angry email help?')]} )")

from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from typing import TypedDict, Annotated, Sequence
import operator
import asyncio

class BaltazarState(TypedDict):
    messages: Annotated[Sequence[HumanMessage], operator.add]
    next: str

def supervisor_node(state):
    last = state["messages"][-1].content.lower()
    if "angry" in last or "reply" in last:
        return {"messages": [HumanMessage(content="Route to rephraser")], "next": "rephraser"}
    elif "steps" in last:
        return {"messages": [HumanMessage(content="Route to stepper")], "next": "stepper"}
    else:
        from consultation_agent import consult_professor_balthazar
        response = asyncio.run(consult_professor_balthazar(last.content, "test_session"))
        return {"messages": [HumanMessage(content=response)], "next": "validator"}

def rephraser_node(state):
    text = state["messages"][-1].content
    from consultation_agent import rephrase_angry  # Your tool
    rephrased = rephrase_angry(text)
    return {"messages": [HumanMessage(content=f"Calmer reply: {rephrased}")], "next": "validator"}

def stepper_node(state):
    problem = state["messages"][-1].content
    from consultation_agent import creative_reframe
    reframe = creative_reframe(problem, "practical")
    steps = reframe["reframed_problem"].split(".")[:3]
    return {"messages": [HumanMessage(content=f"Steps: {' . '.join(steps)}")], "next": "validator"}

def validator_node(state):
    advice = state["messages"][-1].content
    from consultation_agent import validate_response
    valid = validate_response(advice)
    feedback = f"Empathy: {valid['empathy']}/10 | Safe: {valid['safe']}"
    return {"messages": [HumanMessage(content=f"Approved: {feedback}")], "next": END}

workflow = StateGraph(BaltazarState)
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("rephraser", rephraser_node)
workflow.add_node("stepper", stepper_node)
workflow.add_node("validator", validator_node)

workflow.set_entry_point("supervisor")
workflow.add_conditional_edges("supervisor", lambda s: s["next"])
workflow.add_edge("rephraser", "validator")
workflow.add_edge("stepper", "validator")
workflow.add_edge("validator", END)

app = workflow.compile()
print("✅ Multi-agent team ready!")
