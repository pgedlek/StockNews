import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.environ["FINNHUB_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

X_API_KEY = os.environ["X_API_KEY"]
X_API_SECRET = os.environ["X_API_SECRET"]
X_ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
X_ACCESS_TOKEN_SECRET = os.environ["X_ACCESS_TOKEN_SECRET"]

DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

TICKERS = ["NVDA", "AMD", "INTC", "TSM", "ASML", "QCOM", "AVGO"]
