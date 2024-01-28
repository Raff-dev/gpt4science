import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

SERP_API_KEY = os.getenv("SERP_API_KEY")

GPT4 = "gpt-4"
GPT4_TURBO = "gpt-4-1106-preview"
GPT3_TURBO = "gpt-3.5-turbo"

DATA_PATH = BASE_DIR / "data"


# --- CONFIGURATION SETTINGS BELOW --- #

# Number of search queries to generate for Google Scholar
NUMBER_SEARCH_QUERIES = 5
