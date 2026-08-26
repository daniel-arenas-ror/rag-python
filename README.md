
uv venv
source .venv/bin/activate

uv add langchain-anthropic langgraph langsmith fastapi uvicorn slowapi pydantic-settings python-dotenv langchain_openai langchain

uv add --dev pytest httpx 