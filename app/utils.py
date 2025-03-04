import sqlite3
from datetime import datetime
from .config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT,
            output_text TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()

def save_progress(input_text, output_text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO progress (input_text, output_text, timestamp)
        VALUES (?, ?, ?)
    """, (input_text, output_text, datetime.now()))
    conn.commit()
    conn.close()

def speech_to_text(audio_path, whisper_model):
    result = whisper_model.transcribe(audio_path)
    return result["text"]