import json
from jsonschema import validate

def validate_output(raw_output: str, schema: dict) -> dict:
    parsed = json.loads(raw_output)
    validate(instance=parsed, schema=schema)
    return parsed
