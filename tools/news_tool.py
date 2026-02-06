import requests
import os

def get_news(topic):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&pageSize=3&apiKey={api_key}"

    res = requests.get(url).json()

    if res.get("status") != "ok":
        return {"error": "News API failed", "details": res}

    articles = res.get("articles", [])

    return [
        {
            "title": a["title"],
            "source": a["source"]["name"],
            "url": a["url"]
        }
        for a in articles
    ]
