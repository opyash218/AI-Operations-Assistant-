



from tools.weather_tool import get_weather
from tools.github_tool import search_repos
from tools.news_tool import get_news   # NEW

def execute_plan(plan):
    results = []

    for step in plan["steps"]:
        action = step["action"]
        inp = step["input"]

        if action == "weather_tool":
            results.append(get_weather(inp))

        elif action == "github_tool":
            results.append(search_repos(inp))

        elif action == "news_tool":   # NEW
            results.append(get_news(inp))

        else:
            results.append({"error": f"Unknown tool {action}"})

    return results
