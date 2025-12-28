import gradio as gr
from core.csv_loader import CSVLoader
from core.qa_engine import QAEngine

def build_interface(loader: CSVLoader, qa_engine: QAEngine):
    def upload_csv(file):
        status = loader.load_csv(file.name)
        if "✅" in status:
            df = loader.text_data
            resumo = f"O CSV contém {df.count('\n')} linhas após a limpeza."
        else:
            resumo = ""
        return status, resumo, []

    def responder(history, user_input):
        resposta = qa_engine.ask(user_input)
        history.append((user_input, resposta))
        return history, ""

    def limpar_chat():
        return []

    with gr.Blocks(title="RumoGPT", css="""
        .side-bar {
            position: fixed;
            top: 0;
            width: 1%;
            height: 100vh;
            background-color: #003A70;
            z-index: 1;
        }
        .left-bar {
            left: 0;
        }
        .right-bar {
            right: 0;
        }
        .main-content {
            margin-left: 1%;
            margin-right: 1%;
            z-index: 2;
        }
        .header {
            text-align: center;
            margin-top: 10px;
        }
    """) as interface:
        # Barras laterais fixas
        gr.Markdown('<div class="side-bar left-bar"></div>')
        gr.Markdown('<div class="side-bar right-bar"></div>')

        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown(
                    """
                    <div style='width: 100%; text-align: center;'>
                        <h1 style='color: #003A70; font-size: 32px; margin: 10px 0;'>RumoGPT</h1>
                    </div>
                    """,
                    elem_id="header"
                )


        # Conteúdo principal
        with gr.Row(elem_classes="main-content"):
            with gr.Column(scale=2):
                file_input = gr.File(label="➕", file_types=[".csv"], type="filepath", show_label=False)
                file_status = gr.Textbox(visible=False)
                file_summary = gr.Textbox(visible=False)
                gr.Markdown("## 📂 Arquivo Aberto")
                opened_file_display = gr.Textbox(value="Nenhum arquivo carregado.", interactive=False)

            with gr.Column(scale=8):
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Digite sua pergunta...")
                send_btn = gr.Button("Enviar")
                clear_btn = gr.Button("Limpar Chat")

                send_btn.click(responder, inputs=[chatbot, msg], outputs=[chatbot, msg])
                msg.submit(responder, inputs=[chatbot, msg], outputs=[chatbot, msg])
                clear_btn.click(limpar_chat, outputs=[chatbot])

                file_input.change(fn=upload_csv, inputs=file_input, outputs=[file_status, file_summary, chatbot])

            with gr.Column(scale=2):
                gr.Markdown("")  # Espaço reservado para manter layout centralizado

    return interface

