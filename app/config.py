import torch

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
WHISPER_MODEL = "base"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
HF_TOKEN = "your_hugging_face_token_here"  # Replace with actual Hugging Face token
DB_PATH = "data/progress.db"