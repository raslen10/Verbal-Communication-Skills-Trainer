import pytest
from app.model import generate_response

def test_generate_response():
    prompt = "Hello, how are you?"
    response = generate_response(prompt)
    assert isinstance(response, str) and len(response) > 0
