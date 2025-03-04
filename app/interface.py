import gradio as gr
from app.model import generate_response
from app.utils import speech_to_text

def optimize_speech(input_text=None, audio_path=None):
    """
    Optimize a speech for clarity and impact.
    """
    if audio_path:
        # Convert speech to text
        input_text = speech_to_text(audio_path)
    
    if not input_text:
        return "No input provided."
    
    prompt = f"Rewrite the following speech to improve clarity, coherence, and impact:\n\n{input_text}\n\nOptimized version:"
    return generate_response(prompt)
# Gradio Interface
def launch_interface():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🎤 **Verbal Communication Skills Trainer**
        Improve your verbal communication skills with AI!
        
        ✅ Enter text or record your voice
        ✅ Get an improved version of your speech
        ✅ Track your progress
        """)
        
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(lines=5, placeholder="Enter your speech here...", label="📝 Text Input")
                audio_input = gr.Audio(type="filepath", label="🎙️ Voice Input")
                submit_button = gr.Button("🚀 Optimize Speech", variant="primary")
            
            with gr.Column():
                output_text = gr.Textbox(label="✨ Optimized Speech", interactive=False)
                gr.Markdown("**Your improved speech will appear here.**")
        
        submit_button.click(
            optimize_speech,
            inputs=[text_input, audio_input],
            outputs=output_text
        )
        
        gr.Markdown("""
        ### 📊 **Progress Tracking**
        Your inputs and outputs are saved in a database (`progress.db`) for future reference.
        """)
    
    demo.launch()