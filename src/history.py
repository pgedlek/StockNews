"""
Tracks recently used tickers via a local file.
On GitHub Actions this file is persisted between runs using cache.
"""
import json
from pathlib import Path

HISTORY_FILE = Path(__file__).parent.parent / ".ticker_history.json"
MAX_HISTORY = 3  # avoid repeating the same ticker within last 3 posts


def load_recent() -> list[str]:
    if not HISTORY_FILE.exists():
        return []
    return json.loads(HISTORY_FILE.read_text())


def save_recent(ticker: str) -> None:
    recent = load_recent()
    recent.insert(0, ticker)
    HISTORY_FILE.write_text(json.dumps(recent[:MAX_HISTORY]))
