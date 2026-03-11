#1_folder_structure
https://github.com/wawi-m/oaqjp-final-project-emb-ai/blob/main/README.md

#2a_emotion_detection
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

#2b_application_creation
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology")
'{"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'
>>> 

#3a_output_formatting
import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion Predict API and returns detected emotions.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=myobj)

    # Convert response text into dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return results in required format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

#3b_formatted_output_test    
from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology")
{'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167, 'dominant_emotion': 'joy'}

#4a_packaging
__init__.py gitlink

#4b_packaging_test
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I hate working long hours")
{'anger': 0.64949876, 'disgust': 0.03718168, 'fear': 0.05612277, 'joy': 0.00862553, 'sadness': 0.1955148, 'dominant_emotion': 'anger'}
>>> 

#5a_unit_testing
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        # Test case for positive sentiment
        result_1 = emotion_detector('I love working with Python')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for negative sentiment
        result_2 = emotion_detector('I hate working with Python')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for neutral sentiment
        result_3 = emotion_detector('I am neutral on Python')
        self.assertIn(result_3['dominant_emotion'], ['joy','anger','fear','disgust','sadness'])


if __name__ == "__main__":
    unittest.main()

#5b_unit_testing_result
python3.11 test_emotion_detection.py
.
----------------------------------------------------------------------
Ran 1 test in 0.319s

OK
