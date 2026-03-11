import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion Predict API and returns detected emotions.
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=myobj)
    return response.text
