import anthropic
from src.config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = (
    "You are a sharp, opinionated stock market commentator focused on tech and semiconductors. "
    "Your job is to write X (Twitter) posts that spark debate. "
    "Rules: max 280 chars, no URLs, no hedging, take a clear stance, be punchy. "
    "Don't use emojis excessively — one max. No hashtags unless they add punch. "
    "Always use cashtag format for tickers (e.g. $NVDA, $AMD). "
    "When mentioning the main ticker, include its current price naturally in the post (e.g. '$NVDA at $134 and still undervalued')."
)


def generate_post(snapshot: dict) -> str:
    top = snapshot["top_mover"]
    news_headlines = "\n".join(f"- {n['headline']}" for n in snapshot["top_news"])
    quotes_summary = ", ".join(
        f"{q['ticker']} {'+' if q['change_pct'] >= 0 else ''}{q['change_pct']}%"
        for q in snapshot["quotes"]
    )

    if news_headlines:
        news_section = f"Recent news for {top['ticker']}:\n{news_headlines}"
    else:
        news_section = (
            f"No specific news today for {top['ticker']}. "
            "Base your take purely on the price action and broader sector context."
        )

    user_msg = (
        f"Market data:\n{quotes_summary}\n\n"
        f"Biggest mover: {top['ticker']} — current price ${top['price']} ({top['change_pct']:+.2f}%)\n\n"
        f"{news_section}\n\n"
        "Write one punchy X post about this. Use the $TICKER cashtag format. "
        "Include the current price naturally. Take a strong stance. Spark debate."
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=150,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    return response.content[0].text.strip()
