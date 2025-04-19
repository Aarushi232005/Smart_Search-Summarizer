from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, load_tools, AgentType
from langchain.agents import tool
import os

# 🔐 API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
SERPAPI_KEY = os.getenv("SERPAPI_KEY", "8ce6db1f3d27ba013c8f03e069dcc30a7bedcb84b56747278e48176e4d7f9506")

# 🎯 Define Tool
@tool
def greet(name: str) -> str:
    """Greets a person by their name."""  # ✅ this is the required docstring
    return f"Hello, {name}!"


# 🧠 Load LLM and tools
llm = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0.3,
    max_tokens=8000,
    groq_api_key=GROQ_API_KEY,
)

tools = load_tools(["serpapi", "llm-math"], llm=llm, serpapi_api_key=SERPAPI_KEY)
tools.append(greet)

# ⚙️ Initialize agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# 🚀 FastAPI app setup
app = FastAPI()

# 🌐 CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📩 Request schema
class Query(BaseModel):
    query: str

# 📡 POST endpoint
@app.post("/ask")
async def ask_question(query: Query):
    try:
        answer = agent.run(query.query)
        return {"result": answer}
    except Exception as e:
        return {"result": f"Error: {str(e)}"}
