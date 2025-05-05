import whisper
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("small").to(device)
audio_path = "xxxxx"
result = model.transcribe(
    audio_path,
    verbose=True,
    word_timestamps=True)

# create a transcription.txt
f = open("transcription.txt", "w", encoding='utf-8')
f.write(result["text"])
f.close()
