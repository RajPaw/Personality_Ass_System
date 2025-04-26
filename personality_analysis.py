import requests

OPENROUTER_API_KEY = "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"  # New Key I used 
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
        "model": "google/Gemini-flash-1.5",  # make sure model is correct!
        "messages": [
            {"role": "system", "content": "You are a personality assessment assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload)
        result = response.json()

        # Check if "choices" exist
        if "choices" not in result:
            return {"error": result.get("error", "Invalid response from OpenRouter.")}

        personality_result = result["choices"][0]["message"]["content"]
        return {"raw_analysis": personality_result}

    except Exception as e:
        return {"error": str(e)}
