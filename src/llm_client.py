import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "groq").lower()
DEFAULTS = {
    "groq": {
        "model": "openai/gpt-oss-120b",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key_env": "GROQ_API_KEY",
    },
    "ollama": {
        "model": "qwen2.5:3b",
        "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
        "api_key_env": None,
    },
}

if PROVIDER not in DEFAULTS:
    raise ValueError("LLM_PROVIDER must be 'groq' or 'ollama'.")

config = DEFAULTS[PROVIDER]
MODEL = os.getenv("LLM_MODEL") or config["model"]
api_key = os.getenv(config["api_key_env"]) if config["api_key_env"] else "ollama"

if PROVIDER == "groq" and not api_key:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

client = OpenAI(api_key=api_key, base_url=config["base_url"])
