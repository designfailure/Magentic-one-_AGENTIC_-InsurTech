import gradio as gr
from main import initialize_agents

def create_interface():
    agents = initialize_agents()
    
    with gr.Blocks() as app:
        gr.Markdown("# InsurTech MGA Aplikacija")
        
        with gr.Tab("Ocena tveganja"):
            image_input = gr.Image()
            text_output = gr.Textbox()
            
            image_input.change(
                fn=agents["research"].process_image,
                inputs=image_input,
                outputs=text_output
            )
            
    return app

if __name__ == "__main__":
    interface = create_interface()
    interface.launch() 