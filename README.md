# QStockNews 🤖

Automated X bot posting punchy, opinionated takes on tech and semiconductor stocks. Powered by Finnhub market data and Claude AI.

## What it does

- Fetches real-time quotes and news for key semis/tech tickers: **NVDA, AMD, INTC, TSM, ASML, QCOM, AVGO**
- Picks the biggest mover with fresh news (avoids repeating the same ticker)
- Generates a spicy, debate-sparking post via Claude API
- Posts to X automatically 5 times per day during NY market hours

## Posting schedule (ET)

| Time | Context |
|---|---|
| 08:39 | Pre-market setup |
| 10:26 | First hour reaction |
| 12:57 | Midday check-in |
| 15:41 | Last 30min before close |
| 17:52 | After-hours wrap-up |

Weekdays only. Runs via GitHub Actions — no server needed.

## Tech stack

- **Python 3.12**
- **Finnhub API** — market data & news (free tier)
- **Anthropic Claude API** — post generation
- **Tweepy** — X/Twitter posting
- **GitHub Actions** — scheduling (~$0/month)

## Estimated cost

| Service | Cost |
|---|---|
| Finnhub | $0 |
| X API (5 posts/day) | ~$1.50/month |
| Claude API | ~$2–5/month |
| GitHub Actions | $0 |
| **Total** | **~$3–7/month** |

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your API keys
3. Add the same keys as secrets in **GitHub → Settings → Secrets and variables → Actions**
4. Push to `master` — the schedule starts automatically

## Project structure

```
src/
├── config.py          — loads env vars
├── main.py            — entry point
├── history.py         — tracks recently used tickers
├── fetcher/
│   └── finnhub.py     — fetches quotes + news
├── analyzer/
│   └── claude.py      — generates posts via Claude API
├── poster/
│   └── twitter.py     — posts via tweepy
└── scheduler/
    └── jobs.py        — single run() function
.github/workflows/
└── post.yml           — GitHub Actions cron schedule
```

## Manual trigger

Go to **Actions → Post to X → Run workflow** to post immediately.
