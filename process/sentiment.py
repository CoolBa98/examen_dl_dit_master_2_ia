from transformers import pipeline

def analyze_sentiment(transcription):
  sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
  result = sentiment_analyzer(transcription)

  if "1" in result[0]["label"] or "2" in result[0]["label"]:
    return "négatif."
  elif "3" in result[0]["label"]:
    return "neutre."
  else:
    return "positif."
