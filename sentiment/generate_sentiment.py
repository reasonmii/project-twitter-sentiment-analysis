from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np

def preprocess(text):
    new_text = []
 
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def load_sentiment_model():
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    mapping = {0:'negative', 1:'neutral', 2:'positive'}

    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)

    return model


def load_emotion_model():    
    task='emotion'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    mapping = {0:'optimism', 1:'anger', 2:'sadness', 3:'joy'}

    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)

    return model


def get_sentiment(model, data):
    pass