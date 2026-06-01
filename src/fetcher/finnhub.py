import httpx
from datetime import date, timedelta
from src.config import FINNHUB_API_KEY, TICKERS

BASE = "https://finnhub.io/api/v1"
HEADERS = {"X-Finnhub-Token": FINNHUB_API_KEY}


def _get(path: str, params: dict) -> dict:
    r = httpx.get(f"{BASE}{path}", params=params, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def fetch_quotes() -> list[dict]:
    results = []
    for ticker in TICKERS:
        data = _get("/quote", {"symbol": ticker})
        results.append({
            "ticker": ticker,
            "price": data["c"],
            "change_pct": round(data["dp"], 2),
            "high": data["h"],
            "low": data["l"],
        })
    return results


def fetch_news(ticker: str, days_back: int = 1) -> list[dict]:
    today = date.today()
    from_date = (today - timedelta(days=days_back)).isoformat()
    data = _get("/company-news", {
        "symbol": ticker,
        "from": from_date,
        "to": today.isoformat(),
    })
    return [{"headline": item["headline"], "summary": item.get("summary", "")} for item in data[:5]]


def fetch_market_snapshot() -> dict:
    quotes = fetch_quotes()
    movers = sorted(quotes, key=lambda q: abs(q["change_pct"]), reverse=True)

    # Pick the biggest mover that has news; fall back to the biggest mover if none do
    top, news = movers[0], []
    for mover in movers:
        candidate_news = fetch_news(mover["ticker"])
        if candidate_news:
            top, news = mover, candidate_news
            break

    return {"quotes": quotes, "top_mover": top, "top_news": news}
