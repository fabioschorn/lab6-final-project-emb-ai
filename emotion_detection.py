import requests

def emotion_detector(text_to_analyze):
    """Function to detect emotions from given text."""
    # Check if the input is empty
    if not text_to_analyze:
        return "Error: No text provided"
    
    # Check if the input is a string
    if not isinstance(text_to_analyze, str):
        return "Error: Input must be a string"
    
    # Check if the input is too long
    if len(text_to_analyze) > 5000:
        return "Error: Input text is too long. Maximum length is 5000 characters."
    
    # Check if the input contains only whitespace
    if text_to_analyze.isspace():
        return "Error: Input text contains only whitespace"
    
    # Check if the input contains special characters
    if not text_to_analyze.isalnum() and not any(char in text_to_analyze for char in [' ', '.', ',', '!', '?', '-', '_']):
        return "Error: Input text contains unsupported characters"

    # URL for the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers including model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # JSON input for the request
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        result = response.json()
        # Return the 'text' attribute (as instructed)
        return result.get('text', "No text found")
    else:
        return f"Error: {response.status_code}"