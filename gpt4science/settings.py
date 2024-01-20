import os

import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

SERP_API_KEY = os.getenv("SERP_API_KEY")

GPT4 = "gpt-4"
GPT4_TURBO = "gpt-4-1106-preview"
GPT3_TURBO = "gpt3.5-turbo"
