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
