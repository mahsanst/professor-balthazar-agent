# Professor Balthazar's Magic Machine

![Professor Balthazar's Magic Machine Banner](thumbnail.png)

> NOTE: This is a **capstone submission** for the Kaggle Agents Intensive Capstone project 2025. This project demonstrates a creative consultation agent that helps users solve diverse challenges through inventive thinking.

This project contains the core logic for Professor Balthazar's Magic Machine, a creative consultation agent designed to help users overcome challenges through inventive thinking and personalized solutions. The agent is built using Python with async/await patterns and follows a modular architecture, upgraded with multi-agent collaboration via LangGraph for emotional intelligence support, achieving 90% evaluation scores in creative and robustness metrics.

## Problem Statement

People frequently face various challenges in daily life - from creative blocks and decision paralysis to boredom and low motivation. Traditional solutions often provide generic advice that lacks personalization and creative engagement. Manual problem-solving can feel repetitive and draining, especially when facing similar challenges repeatedly. There's a need for an approach that not only solves problems but does so in a way that sparks creativity, maintains engagement, and adapts to individual circumstances through continuous conversation, including handling emotional aspects like anger in workplace interactions.

## Solution Statement

Creative consultation agents can transform mundane problems into engaging opportunities through character-driven dialogue and personalized "inventions." They maintain conversation context across sessions, remembering user details and preferences to provide truly personalized solutions. By reframing challenges as creative puzzles and providing inventive strategies tailored to individual circumstances, these agents make problem-solving an enjoyable and memorable experience. The character persona of an inventive professor adds an element of whimsy while delivering practical solutions across multiple domains including creativity, productivity, and personal growth. Upgrades include multi-agent routing for emotional rephrasing and validation, ensuring empathetic, safe responses, with a Streamlit UI for interactive deployment and Docker for production scalability.

## Architecture

Core to Professor Balthazar is the `consultation_agent` - a sophisticated system for creative problem-solving through continuous dialogue. It's not a simple chatbot but an ecosystem of specialized components working together to provide personalized, inventive solutions. This modular approach, facilitated by Python's async/await patterns and session management, allows for sophisticated conversation flow and context preservation.

The `consultation_agent` is constructed using asynchronous Python functions with robust session management. Its architecture highlights several key components: the `session_manager` for conversation continuity, the `context_tracker` for personalization, and the `creative_reframer` for inventive problem-solving. Crucially, it maintains user context across conversations and adapts its approach based on individual circumstances and problem types. The LangGraph multi-agent upgrade adds supervisor routing, emotional rephrasing, and validation for enhanced robustness, achieving 90% evaluation scores.

The real power of Professor Balthazar lies in its specialized components, each optimized for a specific aspect of the consultation process.

### Context Manager: `user_context_tracker`

This component is responsible for maintaining user details like name, location, mood, and preferences across sessions. It ensures that conversations feel continuous and personalized, building upon previous interactions to create a truly tailored experience. The context tracker allows Professor Balthazar to remember that "Alex in Lisbon" prefers creative solutions over practical ones.

### Creative Engine: `problem_reframer`

Once a problem is identified, the `problem_reframer` transforms it into an creative opportunity. It turns "boredom" into "monochrome canvas waiting for color" and "low energy" into "energetic paradox needing inventive solutions." This component is responsible for the magical, inventive language that makes consultations with Professor Balthazar unique and engaging, now integrated with emotional tools for anger management.

### Solution Generator: `personalized_invention_creator`

After reframing the problem, this component generates tailored strategies and "inventions" based on the user's specific context. For a user in Lisbon feeling uninspired, it might suggest "Lisbon-inspired energy walks" or "task-tuning forks" that incorporate local elements into the solution. The multi-agent upgrade routes to specialized rephrasers and validators for empathetic outputs.

### Session Orchestrator: `dialogue_manager`

This component manages the flow of conversation, ensuring that Professor Balthazar's responses maintain character consistency while advancing the consultation toward practical solutions. It handles the balance between creative whimsy and actionable advice that defines the agent's unique value proposition, enhanced by LangGraph for team collaboration.

## Essential Tools and Utilities

The `consultation_agent` and its components are equipped with specialized tools to perform their tasks effectively.

### Session Management (`session_manager`)

A crucial tool that maintains conversation continuity through unique session IDs, allowing the agent to remember user context and build upon previous discussions. This enables truly continuous conversations where Professor Balthazar can recall past challenges and solutions, upgraded with 90% evaluation scores for robustness.

### Character Consistency (`persona_engine`)

This tool ensures that Professor Balthazar maintains consistent personality, speech patterns, and inventive vocabulary throughout all interactions. It's responsible for the agent's unique voice and the magical, inventive language that makes consultations engaging, now with emotional rephrasing for anger scenarios.

### Solution Archiver (`consultation_archiver`)

This tool saves user problems and generated solutions to "Professor's archives," enabling potential future analysis and continuous improvement of the consultation process. It also allows for tracking solution effectiveness over time, integrated with Docker deployment for production scalability.

## File Structure

- **consultation_agent.py**: Core agent logic with tools, memory, and helper functions (original + emotional upgrades).
- **app.py**: Streamlit UI for interactive chat interface.
- **eval.py**: Day 4 evaluation script (90% creative/robustness scores).
- **graph.py**: LangGraph multi-agent team for routing and collaboration.
- **Test.py**: Unit tests for agent functionality and upgrades.
- **requirements.txt**: Dependencies for running the project.
- **Dockerfile**: Production deployment configuration.
- **.env.example**: Template for API key setup (use Kaggle Secrets).
- **thumbnail.png**: Project thumbnail for capstone submission.
- **README.md**: This file—project documentation and usage.

## Installation & Usage

### Quick Start
```bash
pip install -r requirements.txt
python consultation_agent.py  # Run standalone
```

### Run Demo
```python
import asyncio
from consultation_agent import demonstrate_magic_machine

asyncio.run(demonstrate_magic_machine())
```

### Run Streamlit UI
```bash
streamlit run app.py
```

### Run Evals
```python
python eval.py
```

### Docker Deployment
```bash
docker build -t balthazar .
docker run -p 8501:8501 balthazar
```

## Team Contributions
- **Azam Kheyri**: Core agent architecture, creative reframing tools, memory system
- **Mahsa Nadifar**: Multi-agent LangGraph integration, emotional rephrasing tools, evals, Streamlit UI, Docker deployment
- **Parisa Ahmadi Ghotbi**: Prompt engineering, testing, deployment optimization

```
