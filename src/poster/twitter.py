import tweepy
from src.config import X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, DRY_RUN


def _client() -> tweepy.Client:
    return tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET,
    )


def post(text: str) -> str | None:
    if len(text) > 280:
        text = text[:277] + "..."
    if DRY_RUN:
        print(f"[DRY RUN] Would post: {text}")
        return None
    response = _client().create_tweet(text=text)
    return str(response.data["id"])
