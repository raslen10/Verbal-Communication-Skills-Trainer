import pytest
from app.interface import optimize_speech

def test_optimize_speech():
    input_text = "This is a test speech."
    output_text = optimize_speech(input_text=input_text)
    assert isinstance(output_text, str) and len(output_text) > 0
