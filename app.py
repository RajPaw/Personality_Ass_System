from flask import Flask, request, jsonify
from flask_cors import CORS
from personality_analysis import analyze_personality

app = Flask(__name__)
CORS(app)

# In-memory storage (can switch to DB later)
candidate_profiles = {}

@app.route("/submit-response", methods=["POST"])
def submit_response():
    data = request.json
    candidate_id = data.get("candidate_id")
    responses = data.get("responses")

    if not candidate_id or not responses:
        return jsonify({"error": "Missing candidate_id or responses"}), 400

    profile = analyze_personality(responses)
    candidate_profiles[candidate_id] = profile

    return jsonify({"message": "Personality analyzed", "profile": profile})

@app.route("/get-profile/<candidate_id>", methods=["GET"])
def get_profile(candidate_id):
    profile = candidate_profiles.get(candidate_id)
    if profile:
        return jsonify({"profile": profile})
    return jsonify({"error": "Profile not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
