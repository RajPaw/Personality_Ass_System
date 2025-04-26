import requests

OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_personality(responses):
    prompt = f"""You are a psychologist AI. Analyze the following behavioral responses based on the Big Five Personality Traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism).

Responses:
{responses}

Give a score from 0 to 100 for each trait, and give 1-2 line feedback for each."""

    payload = {
        "model": "google/Gemini-flash-1.5",
        "messages": [
            {"role": "system", "content": "You are a personality assessment assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload)
        result = response.json()
        personality_result = result["choices"][0]["message"]["content"]
        return {"raw_analysis": personality_result}
    except Exception as e:
        return {"error": str(e)}
