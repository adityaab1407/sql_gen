import gradio as gr
import subprocess
import pandas as pd
from backend import *


def main():
    with gr.Blocks() as frontend:
        gr.Markdown("# SQL Generator Tool")
        gr.Markdown("### Describe your task, and the tool will analyze your workspace, generate SQL, and execute it.")
        
        operation = gr.Textbox(label="Describe your task")
        
        with gr.Row():
            analyze_btn = gr.Button("Analyze Workspace", variant="primary")
            reset_btn = gr.Button("Reset")
        
        with gr.Row():
            input1 = gr.Dataframe(label="Input 1")
            input2 = gr.Dataframe(label="Input 2")
        
        with gr.Row():
            generate_btn = gr.Button("Generate Formula", variant="primary")
        
        with gr.Row():
            generated_sql = gr.Textbox(label="Generated SQL Formula", interactive=False)
        
        with gr.Row():
            execute_btn = gr.Button("Execute!", variant="primary")
            go_back_btn = gr.Button("Reset")
        
        with gr.Row():
            query_results = gr.Dataframe(label="Query Results")
            
        # Actions
        analyze_btn.click(run_source_detector, outputs=[input1, input2]) 
        generate_btn.click(generate_sql, inputs=operation, outputs=[generated_sql, operation])  
        execute_btn.click(run_executor, outputs=query_results)  
        reset_btn.click(lambda: "", outputs=operation) 
        go_back_btn.click(lambda: "", outputs=generated_sql) 

    frontend.launch()

if __name__ == "__main__":
    main()
