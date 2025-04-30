"""Flask server for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Render the index HTML page with input form.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Process user input and return emotion analysis results or error message.
    """
    text_to_analyze = request.form.get("textToAnalyze", "").strip()
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return render_template("index.html", error="Invalid text! Please try again.")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)