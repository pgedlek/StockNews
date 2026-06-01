import logging
from src.fetcher.finnhub import fetch_market_snapshot
from src.analyzer.claude import generate_post
from src.poster.twitter import post

logger = logging.getLogger(__name__)


def run() -> None:
    """Fetch → generate → post. One shot."""
    snapshot = fetch_market_snapshot()
    text = generate_post(snapshot)
    logger.info(f"Generated: {text}")
    tweet_id = post(text)
    logger.info(f"Posted tweet_id={tweet_id}")
