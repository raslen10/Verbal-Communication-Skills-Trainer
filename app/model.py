import whisper
from transformers import AutoModelForCausalLM, AutoTokenizer
from .config import MODEL_NAME, WHISPER_MODEL, DEVICE, HF_TOKEN

def load_models():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, load_in_8bit=True, device_map="auto", use_auth_token=HF_TOKEN
    )
    whisper_model = whisper.load_model(WHISPER_MODEL)
    return tokenizer, model, whisper_model

tokenizer, model, whisper_model = load_models()
