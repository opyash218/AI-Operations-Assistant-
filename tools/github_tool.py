import requests

def search_repos(query):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    res = requests.get(url).json()

    top = res["items"][:3]
    return [
        {"name": r["name"], "stars": r["stargazers_count"], "url": r["html_url"]}
        for r in top
    ]
