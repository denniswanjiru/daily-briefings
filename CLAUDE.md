# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Daily Briefings is an AI-powered daily briefings dashboard using a multi-agent system built with LangChain and LangGraph. The application generates personalized daily briefings by orchestrating four specialized agents through a LangGraph workflow.

## Key Commands

### Development
```bash
# Install dependencies
poetry install

# Run the application
poetry run python -m app.main
# OR with auto-reload
poetry run uvicorn app.main:app --reload

# Access API documentation
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Testing
```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_agents.py

# Run with coverage
poetry run pytest --cov=app tests/

# Run specific test
poetry run pytest tests/test_agents.py::TestPlannerAgent::test_planner_invoke
```

### Code Quality
```bash
# Format code
poetry run black app/ tests/

# Lint code
poetry run ruff check app/ tests/

# Type checking
poetry run mypy app/
```

## Architecture

### Multi-Agent Workflow (LangGraph)

The core architecture is a **LangGraph state machine** that orchestrates four agents in sequence:

1. **Load Context** → 2. **Planner Agent** → 3. **[Motivator Agent + Wellness Agent in parallel]** → 4. **Summary Agent**

#### State Flow (app/agents/graph.py)
- **BriefingState (TypedDict)**: Shared state passed between agents containing:
  - Input: `user_id`, `preferences`, `context`
  - Data: `calendar_events`, `tasks`, `priorities`
  - Agent outputs: `planner_output`, `motivator_output`, `wellness_output`, `summary_output`
  - Metadata: `errors`

#### Agent Pattern
All agents in `app/agents/` follow the same pattern:
- Initialize with an LLM instance (`BaseChatModel`)
- Define a `system_prompt` for agent behavior
- Implement `async invoke(state: Dict[str, Any]) -> Dict[str, Any]` that:
  1. Extracts relevant data from state
  2. Builds prompts for LLM
  3. Calls LLM with system + user messages
  4. Parses response and updates state

#### Parallel Execution
The graph executes motivator and wellness agents in parallel after planner completes (both depend on `planner_output`), then waits for both before running summary.

### Configuration System (app/core/config.py)

Uses **Pydantic Settings** with environment variable loading:
- Global singleton: `settings` instance loaded from `.env`
- LLM provider abstraction: supports `openai` and `anthropic` via `llm_provider` setting
- All API keys and config loaded through Pydantic validation

### API Layer (FastAPI)

**app/main.py**: FastAPI app with:
- Health check routes (`/health/`, `/health/ready`, `/health/live`)
- Dashboard routes (`/dashboard/briefing`, `/dashboard/data/{user_id}`)
- CORS middleware (currently wide open, needs production restriction)
- Startup/shutdown hooks for resource initialization

**API Request Flow**:
1. Request → `routes_dashboard.py:generate_briefing()`
2. Create graph → `graph.py:create_briefing_graph()`
3. Invoke graph with user state → graph executes agent workflow
4. Return `BriefingResponse` with all agent outputs

### Services Layer

**app/services/calendar_service.py**:
- `CalendarService` class with provider abstraction (Google, Outlook)
- Methods: `get_events()`, `get_today_events()`, `get_upcoming_events()`
- Currently returns placeholder data; needs OAuth implementation

**app/services/user_memory.py**:
- `UserMemory` class for user profiles, tasks, preferences, briefing history
- Currently in-memory dict; designed to be backed by database
- Methods: `get_user_profile()`, `get_user_tasks()`, `save_briefing_history()`

### Schemas (Pydantic Models)

**app/schemas/user.py**: `UserProfile`, `UserPreferences`, `Task`, `CalendarEvent`
**app/schemas/dashboard.py**: Request/response models for API:
- `BriefingRequest` → `BriefingResponse`
- `DashboardData` for user dashboard views
- Individual agent output models: `PlannerOutput`, `MotivatorOutput`, `WellnessOutput`, `SummaryOutput`

## Current State & TODOs

The codebase is a **skeleton implementation** with extensive TODOs. Core structure is complete but agents need:

1. **LLM Integration**: Uncomment and implement LLM initialization in `create_briefing_graph()`
   - Use `settings.llm_provider` to determine which LLM client to instantiate
   - Import `langchain_openai.ChatOpenAI` or `langchain_anthropic.ChatAnthropic`

2. **Graph Wiring**: In `graph.py`, uncomment and complete:
   - Node definitions (`workflow.add_node()`)
   - Edge definitions (`workflow.add_edge()`)
   - Graph compilation (`workflow.compile()`)

3. **Agent Implementation**: Each agent needs:
   - Prompt engineering in `_build_prompt()` methods
   - Response parsing in `_parse_*()` methods
   - Error handling and retry logic

4. **Service Implementation**:
   - Calendar: OAuth flows for Google/Outlook
   - User Memory: Database backend (replace in-memory dict)

5. **Testing**: All test files have skeleton structure with `pass` statements

## Environment Setup

Required in `.env` (copy from `.env.example`):
- `LLM_PROVIDER`: "openai" or "anthropic"
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
- Optional: `DATABASE_URL` for persistent storage
- Optional: Calendar API credentials

## Important Patterns

### Adding a New Agent
1. Create agent class in `app/agents/` with `__init__(llm)` and `async invoke(state)`
2. Update `BriefingState` TypedDict in `graph.py` with new output field
3. Add node to graph in `create_briefing_graph()`
4. Wire edges to define execution order
5. Add corresponding schema in `app/schemas/dashboard.py`

### LLM Provider Switching
The design supports multiple LLM providers through `settings.llm_provider`. When implementing, use:
```python
if settings.llm_provider == "openai":
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model=settings.llm_model, temperature=settings.llm_temperature)
elif settings.llm_provider == "anthropic":
    from langchain_anthropic import ChatAnthropic
    llm = ChatAnthropic(model=settings.llm_model, temperature=settings.llm_temperature)
```

### State Management
Always pass the full state dict between agents. Each agent:
- Reads from state (e.g., `state.get("planner_output")`)
- Adds its output to state (e.g., `state["motivator_output"] = result`)
- Returns the modified state
