
uv venv
source .venv/bin/activate

uv add langchain-anthropic langgraph langsmith fastapi uvicorn slowapi pydantic-settings python-dotenv langchain_openai langchain

uv add --dev pytest httpx 

Run Test
uv run pytest tests/test_security.py -v

Run API
uv run uvicorn app.main:app --reload --port 8000
