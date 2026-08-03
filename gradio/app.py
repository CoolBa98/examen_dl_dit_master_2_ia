import gradio as gr
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from process.transcription import transcribe_audio
from process.sentiment import analyze_sentiment

def pipeline(audio_file):
  text = transcribe_audio(audio_file)
  sentiment = analyze_sentiment(text)
  return f"Transcription: {text}\nSentiment: {sentiment}"

iface = gr.Interface(
  fn=pipeline,
  inputs=gr.Audio(type="filepath"),
  outputs="text",
  title="Analyse de sentiment à partir d'un fichier audio d'un client",
)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 7860))
  iface.launch(server_name="0.0.0.0", server_port=port)
