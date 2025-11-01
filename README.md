# Daily Briefings

An AI-powered daily briefings dashboard that provides personalized planning, motivation, and wellness insights using LangChain and LangGraph agents.

## Features

- **Intelligent Planning**: AI agent analyzes your calendar and tasks to create an optimized daily schedule
- **Personalized Motivation**: Generates custom motivational content based on your goals and progress
- **Wellness Recommendations**: Provides health and wellness tips tailored to your schedule
- **Comprehensive Briefings**: Synthesizes all insights into a cohesive daily briefing

## Architecture

The application uses a multi-agent system built with LangChain and LangGraph:

- **Planner Agent**: Analyzes calendar events and tasks to create an optimized schedule
- **Motivator Agent**: Generates personalized motivational content
- **Wellness Agent**: Provides health and wellness recommendations
- **Summary Agent**: Compiles all outputs into a coherent briefing

## Project Structure

```
daily-briefings/
├── app/
│   ├── main.py                # FastAPI entrypoint
│   ├── api/                   # API routes
│   │   ├── routes_dashboard.py
│   │   └── routes_health.py
│   ├── core/                  # Core configuration
│   │   ├── config.py          # Environment variables
│   │   └── logger.py          # Logging setup
│   ├── agents/                # LangChain agents
│   │   ├── planner_agent.py
│   │   ├── motivator_agent.py
│   │   ├── wellness_agent.py
│   │   ├── summary_agent.py
│   │   └── graph.py           # LangGraph workflow
│   ├── services/              # Business logic
│   │   ├── calendar_service.py
│   │   └── user_memory.py
│   ├── schemas/               # Pydantic models
│   │   ├── dashboard.py
│   │   └── user.py
│   └── utils/                 # Utilities
│       ├── text_cleaner.py
│       └── time_helpers.py
├── tests/
│   ├── test_agents.py
│   ├── test_api.py
│   └── test_graph_flow.py
├── .env.example
├── pyproject.toml
└── README.md
```

## Setup

### Prerequisites

- Python 3.12+
- Poetry (for dependency management)

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd daily-briefings
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Set up environment variables:

```bash
cp .env.example .env
# Edit .env and add your API keys and configuration
```

4. Configure your LLM provider:
   - For OpenAI: Add your `OPENAI_API_KEY` to `.env`
   - For Anthropic: Add your `ANTHROPIC_API_KEY` to `.env`

### Running the Application

Start the FastAPI server:

```bash
poetry run python -m app.main
```

Or using uvicorn directly:

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health Checks

- `GET /health/` - Basic health check
- `GET /health/ready` - Readiness check with dependencies
- `GET /health/live` - Liveness check

### Dashboard

- `POST /dashboard/briefing` - Generate a daily briefing
- `GET /dashboard/data/{user_id}` - Get dashboard data for a user
- `POST /dashboard/feedback` - Submit feedback on a briefing

## Development

### Running Tests

```bash
poetry run pytest
```

Run with coverage:

```bash
poetry run pytest --cov=app tests/
```

### Code Formatting

The project uses Black for code formatting and Ruff for linting:

```bash
# Format code
poetry run black app/ tests/

# Lint code
poetry run ruff check app/ tests/

# Type checking
poetry run mypy app/
```

## Configuration

### Environment Variables

Key configuration options (see `.env.example` for full list):

- `LLM_PROVIDER`: Choose between "openai" or "anthropic"
- `LLM_MODEL`: Specify the model to use
- `DEBUG`: Enable debug mode
- `DATABASE_URL`: Optional database connection for persistent storage

### Calendar Integration

To integrate with calendar services:

1. **Google Calendar**:

   - Set up Google Calendar API credentials
   - Add credentials path to `GOOGLE_CALENDAR_CREDENTIALS`

2. **Outlook Calendar**:
   - Register an app in Azure AD
   - Add `OUTLOOK_CLIENT_ID` and `OUTLOOK_CLIENT_SECRET`

## TODO & Next Steps

The current implementation provides a skeleton structure. To complete the project:

1. **Agent Implementation**:

   - Complete LLM prompt engineering for each agent
   - Implement response parsing and validation
   - Add error handling and retry logic

2. **LangGraph Workflow**:

   - Complete the graph definition in `graph.py`
   - Implement parallel execution for motivator and wellness agents
   - Add state management and checkpointing

3. **Calendar Integration**:

   - Implement Google Calendar API client
   - Add Outlook Calendar support
   - Handle authentication and token refresh

4. **User Memory**:

   - Add database backend (PostgreSQL, MongoDB, etc.)
   - Implement user preference learning
   - Add briefing history storage

5. **Testing**:

   - Complete unit tests for all agents
   - Add integration tests for the full workflow
   - Implement end-to-end API tests

6. **Production Readiness**:
   - Add rate limiting
   - Implement caching for frequently accessed data
   - Set up monitoring and logging
   - Add authentication and authorization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

[Add your license here]

## Support

For issues and questions, please open a GitHub issue.
