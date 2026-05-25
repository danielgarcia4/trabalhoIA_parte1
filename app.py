import gradio as gr

from src.agent.controller import run_agent

from src.tools.active_recall import (
    gerar_pergunta,
    avaliar_resposta
)

from src.tools.difficulty_tools import (
    identificar_dificuldades,
    recomendar_revisao
)

pergunta_atual = ""

# ======================================
# CHAT
# ======================================

def respond(message, history):

    response = run_agent(message)

    if history is None:
        history = []

    history.append({
        "role": "user",
        "content": message
    })

    history.append({
        "role": "assistant",
        "content": str(response)
    })

    return history, ""

# ======================================
# ACTIVE RECALL
# ======================================

def iniciar_recall(topic):

    global pergunta_atual

    pergunta_atual = gerar_pergunta(topic)

    return pergunta_atual

def responder_recall(
    topic,
    resposta
):

    global pergunta_atual

    feedback = avaliar_resposta(
        topic,
        pergunta_atual,
        resposta
    )

    return feedback

# ======================================
# INTERFACE
# ======================================

with gr.Blocks() as app:

    gr.Markdown("# JARVIS Acadêmico")

    # ==================================
    # ASSISTENTE
    # ==================================

    with gr.Tab("Assistente"):

        chatbot = gr.Chatbot()

        msg = gr.Textbox(
            label="Mensagem"
        )

        send_btn = gr.Button(
            "Enviar"
        )

        send_btn.click(
            fn=respond,
            inputs=[msg, chatbot],
            outputs=[chatbot, msg]
        )

    # ==================================
    # ACTIVE RECALL
    # ==================================

    with gr.Tab("Active Recall"):

        topic_input = gr.Textbox(
            label="Tema"
        )

        pergunta_output = gr.Textbox(
            label="Pergunta"
        )

        gerar_btn = gr.Button(
            "Gerar Pergunta"
        )

        resposta_input = gr.Textbox(
            label="Sua resposta"
        )

        feedback_output = gr.Textbox(
            label="Feedback"
        )

        avaliar_btn = gr.Button(
            "Avaliar"
        )

        gerar_btn.click(
            fn=iniciar_recall,
            inputs=[topic_input],
            outputs=[pergunta_output]
        )

        avaliar_btn.click(
            fn=responder_recall,
            inputs=[
                topic_input,
                resposta_input
            ],
            outputs=[feedback_output]
        )

    # ==================================
    # DIFICULDADES
    # ==================================

    with gr.Tab("Dificuldades"):

        dificuldades_btn = gr.Button(
            "Ver dificuldades"
        )

        dificuldades_output = gr.Textbox(
            label="Dificuldades"
        )

        recomendacao_btn = gr.Button(
            "Recomendar revisão"
        )

        recomendacao_output = gr.Textbox(
            label="Recomendação"
        )

        dificuldades_btn.click(
            fn=identificar_dificuldades,
            inputs=[],
            outputs=[dificuldades_output]
        )

        recomendacao_btn.click(
            fn=recomendar_revisao,
            inputs=[],
            outputs=[recomendacao_output]
        )

app.launch()