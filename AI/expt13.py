from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

questions = [
    "Do you like premium luxury items?",
    "Do you attend formal events often?",
    "Do you prefer classic watch designs?",
    "Do you like sporty looks?",
    "Do you want a watch for daily use?",
    "Do you prefer affordable watches?",
    "Do you like metal straps?",
    "Do you like leather straps?",
    "Do you travel frequently?",
    "Do you prefer lightweight watches?",
    "Do you like bold dial designs?",
    "Do you wear watches mainly for fashion?",
    "Do you like vintage style watches?",
    "Do you prefer simple minimal designs?",
    "Do you go to college or office daily?",
    "Do you like durable watches?",
    "Do you prefer branded accessories?",
    "Do you like black dial watches?",
    "Do you prefer elegant watches over sporty ones?",
    "Do you want a long-lasting watch?"
]

BRAND_INFO = {
    "ROLEX":  {"tagline": "Best for luxury, premium style, and elegance.",  "emoji": "👑"},
    "FOSSIL": {"tagline": "Best for fashion and stylish casual wear.",       "emoji": "🕶️"},
    "CASIO":  {"tagline": "Best for sporty, durable, and everyday use.",    "emoji": "⚡"},
    "TITAN":  {"tagline": "Best for office, formal, and minimal style.",    "emoji": "💼"},
    "TIMEX":  {"tagline": "Best for comfort, simplicity, and daily wear.",  "emoji": "🌿"},
}

def calculate_scores(answers: list[bool]) -> dict:

    rolex = fossil = casio = titan = timex = 0

    scoring_map = {
        "rolex":  [0, 1, 6, 11, 16, 18],
        "fossil": [2, 7, 10, 11, 12],
        "casio":  [3, 5, 9, 15, 19],
        "titan":  [4, 13, 14, 18, 19],
        "timex":  [5, 8, 9, 13, 15],
    }

    scores = {brand: 0 for brand in scoring_map}
    for brand, indices in scoring_map.items():
        for i in indices:
            if answers[i]:
                scores[brand] += 2

    return scores


@app.route("/api/questions", methods=["GET"])
def get_questions():

    return jsonify({
        "questions": [{"id": i, "text": q} for i, q in enumerate(questions)]
    })


@app.route("/api/recommend", methods=["POST"])
def recommend():

    data = request.get_json(silent=True)
    if not data or "answers" not in data:
        return jsonify({"error": "Missing 'answers' field in request body."}), 400

    answers = data["answers"]
    if len(answers) != len(questions):
        return jsonify({
            "error": f"Expected {len(questions)} answers, got {len(answers)}."
        }), 400

    if not all(isinstance(a, bool) for a in answers):
        return jsonify({"error": "All answers must be boolean (true/false)."}), 400

    scores = calculate_scores(answers)
    top_brand = max(scores, key=scores.get).upper()

    return jsonify({
        "scores": {k.upper(): v for k, v in scores.items()},
        "recommendation": {
            "brand":   top_brand,
            "tagline": BRAND_INFO[top_brand]["tagline"],
            "emoji":   BRAND_INFO[top_brand]["emoji"],
        }
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)