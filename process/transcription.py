import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

def transcribe_audio(audio_path):

  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
  model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

  waveform, sample_rate = torchaudio.load(audio_path)
  if waveform.shape[0] > 1:
    waveform = waveform.mean(dim=0, keepdim=True)
  if sample_rate != 16000:
    waveform = torchaudio.functional.resample(waveform, sample_rate, 16000)

  input_values = processor(waveform.squeeze(), return_tensors="pt", sampling_rate = 16000).input_values

  with torch.no_grad():
    logits = model(input_values).logits
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = processor.decode(predicted_ids[0])

  return transcription
