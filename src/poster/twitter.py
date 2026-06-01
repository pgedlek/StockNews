import re
import tweepy
from src.config import X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, DRY_RUN


def _client() -> tweepy.Client:
    return tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET,
    )


def _enforce_single_cashtag(text: str) -> str:
    """Keep only the first cashtag, replace the rest with just the ticker name."""
    cashtags = re.findall(r'\$([A-Z]{1,5})\b', text)
    if len(cashtags) <= 1:
        return text
    for ticker in cashtags[1:]:
        text = re.sub(rf'\${ticker}\b', ticker, text)
    return text


def post(text: str) -> str | None:
    text = _enforce_single_cashtag(text)
    if len(text) > 280:
        text = text[:277] + "..."
    if DRY_RUN:
        print(f"[DRY RUN] Would post: {text}")
        return None
    response = _client().create_tweet(text=text)
    return str(response.data["id"])
