import requests

def emotion_detector(text_to_analyze):
    """Function to detect emotions from given text."""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()

        try:
            emotions = result["emotionPredictions"][0]["emotion"]

            # Extract individual scores
            anger_score = emotions.get("anger", 0)
            disgust_score = emotions.get("disgust", 0)
            fear_score = emotions.get("fear", 0)
            joy_score = emotions.get("joy", 0)
            sadness_score = emotions.get("sadness", 0)

            # Find the dominant emotion (emotion with highest score)
            emotion_scores = {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return the full formatted dictionary
            return {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score,
                "dominant_emotion": dominant_emotion
            }

        except (KeyError, IndexError):
            return {"message": "Emotion predictions not found"}
    else:
        return {"message": f"Error {response.status_code}"}