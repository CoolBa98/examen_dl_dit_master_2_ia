import sys
import os
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, File, UploadFile
from process.transcription import transcribe_audio
from process.sentiment import analyze_sentiment


app = FastAPI()

def pipeline(audio_file):
  text = transcribe_audio(audio_file)
  sentiment = analyze_sentiment(text)
  return (text, sentiment)

@app.get("/")
def entree():
  return {"message": "API EXAMEN DEEP LEARNING 2 DIT"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
  file_path = os.path.join(os.getcwd(), "temp_audio.wav")
  with open(file_path, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  transcription, sentiment =  pipeline(file_path)
  os.remove(file_path)

  return {"transcription": transcription, "sentiment": sentiment}

if __name__ == "__main__":
  import uvicorn
  port = int(os.environ.get("PORT", 8000))
  uvicorn.run("main:app", host="0.0.0.0", port=port)
