from fastapi import FastAPI, HTTPException
from registry import PROMPTS
from llm_gateway import call_llm
from validator import validate_output

app = FastAPI(title="Cortex LLM Core – Phase 1")

@app.post("/jobs/keyword-extraction")
def keyword_extraction(payload: dict):
    text = payload.get("text")
    if not text:
        raise HTTPException(400, "text is required")

    entry = PROMPTS["keyword_extraction:v1"]
    prompt = entry["template"].replace("{{text}}", text)
    schema = entry["schema"]

    raw = call_llm(prompt)

    try:
        validated = validate_output(raw, schema)
    except Exception as e:
        raise HTTPException(500, f"Schema validation failed: {e}")

    return {
        "status": "SUCCESS",
        "data": validated
    }

@app.get("/")
def health_check():
    return {
        "status": "OK",
        "service": "Cortex LLM Core",
        "phase": "Phase-1",
        "message": "LLM Core API is running",
        "developer": "Sourav"
    }
