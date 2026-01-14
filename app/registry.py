PROMPTS = {
    "keyword_extraction:v1": {
        "template": (
            "Extract keywords from the text below.\n"
            "Return ONLY valid JSON matching this schema:\n"
            "{ \"keywords\": [\"string\"] }\n\n"
            "Text:\n{{text}}"
        ),
        "schema": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["keywords"]
        }
    }
}
