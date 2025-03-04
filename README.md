# Verbal-Communication-Skills-Trainer

## 📌 Overview
This project is an AI-powered verbal communication skills trainer. It allows users to input text or voice recordings, which are then optimized for clarity and impact using a language model. The application features a **dark/light mode toggle** and tracks user progress in a SQLite database.

## 📂 Project Structure
```
project_root/
│── app/
│   ├── config.py         # Configuration settings (model names, device, etc.)
│   ├── model.py          # Loads AI models (Whisper & Mistral)
│   ├── interface.py      # Gradio UI implementation
│   ├── utils.py          # Utility functions (speech-to-text, progress saving, etc.)
│
│── data/
│   ├── prompts.json      # Predefined prompts for text generation
│   ├── progress.db       # SQLite database storing user progress
│
│── tests/
│   ├── test_model.py     # Unit tests for model performance
│   ├── test_interface.py # UI and API endpoint tests
│
│── main.py               # Entry point to launch the app
│── requirements.txt      # Dependencies for the project
│── README.md             # Documentation and setup instructions
```

## 🛠 Installation & Setup
### 1️⃣ Install dependencies
Make sure you have Python installed (>=3.8), then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Set up the database
Run the following command to initialize the SQLite database:
```bash
python main.py --init-db
```

### 3️⃣ Run the application
Launch the Gradio interface using:
```bash
python main.py
```
The app will be available at `http://localhost:7860/`

## 📝 Usage Example
1. **Text Input**: Enter a speech text and click "Optimize Speech."
2. **Voice Input**: Record your voice, and the AI will transcribe & optimize it.
3. **Dark Mode Toggle**: Enable dark mode for better UI experience.
4. **Tracking Progress**: All inputs and outputs are saved in `progress.db`.

## 🧪 Running Tests
To ensure the application works correctly, run the test suite:
```bash
pytest tests/
```

## 🚀 Future Enhancements
- Support for multiple languages
- Advanced AI tuning for better speech optimization
- Cloud-based progress tracking

### 🎤 **Enhance Your Speaking Skills Today!** 🚀

