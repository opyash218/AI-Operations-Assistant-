import json
from llm.llm_client import call_llm

VERIFIER_PROMPT = """
You are a verification agent.
Ensure the output is complete and structured as JSON.
Fix missing fields if possible.
"""


def verify_output(data):
    try:
        return call_llm(VERIFIER_PROMPT, json.dumps(data))
    except:
        return {"verified_output": data}