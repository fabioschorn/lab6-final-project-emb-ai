# server.py

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create Flask app
app = Flask(__name__)

# Route to home page (index.html)
@app.route('/')
def render_index_page():
    return render_template('index.html')

# Route to detect emotion
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Get text from the form
    text_to_analyze = request.form['textToAnalyze']

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check if the response is valid
    if response is None or not isinstance(response, dict):
        return "Invalid response from emotion detection service"

    # Extract emotions
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', '')

    # Format the output like required
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output_message

# Run app on port 5000
if __name__ == "__main__":
    app.run(debug=True)