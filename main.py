from fastapi import FastAPI
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_output

app = FastAPI()

@app.post("/run-task")
def run_task(task: str):
    plan = create_plan(task)
    results = execute_plan(plan)
    final = verify_output(results)

    return {
        "plan": plan,
        "results": results,
        "final_output": final
    }
