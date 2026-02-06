import json
from llm.llm_client import call_llm

PLANNER_PROMPT = """
You are a planning agent.
Convert user requests into structured execution plans.

Output STRICT JSON:
{
  "steps": [
    {
      "step_id": 1,
      "action": "tool_name",
      "input": "what to pass"
    }
  ]
}
"""





def create_plan(user_task: str):
    try:
        raw_plan = call_llm(PLANNER_PROMPT, user_task)
        return json.loads(raw_plan)

    except Exception as e:
        print("LLM failed, using fallback planner:", e)
        task = user_task.lower()

        if "weather" in task:
            city = user_task.split("in")[-1].strip()
            return {"steps": [{"step_id": 1, "action": "weather_tool", "input": city}]}

        if "github" in task or "repo" in task:
            return {"steps": [{"step_id": 1, "action": "github_tool", "input": "machine learning"}]}

        if "news" in task or "headline" in task:
            topic = user_task.split("about")[-1].strip() if "about" in task else "technology"
            return {"steps": [{"step_id": 1, "action": "news_tool", "input": topic}]}

        return {"steps": []}