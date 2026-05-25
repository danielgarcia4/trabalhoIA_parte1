from src.llm.client import ask_llm

from src.database.performance_db import (
    save_performance
)

def gerar_pergunta(topic):

    prompt = f"""
    Gere uma pergunta de active recall sobre:

    {topic}
    """

    return ask_llm(prompt)

def avaliar_resposta(
    topic,
    question,
    answer
):

    prompt = f"""
    Você é um professor.

    Avalie a resposta do aluno.

    Tema:
    {topic}

    Pergunta:
    {question}

    Resposta do aluno:
    {answer}

    Dê:
    - uma nota de 0 a 10
    - um feedback curto

    Formato:

    NOTA: X
    FEEDBACK: texto
    """

    evaluation = ask_llm(prompt)

    print("\nAVALIAÇÃO:")
    print(evaluation)

    # ==================================
    # EXTRAÇÃO DA NOTA
    # ==================================

    score = 0

    try:

        lines = evaluation.split("\n")

        for line in lines:

            if "NOTA" in line.upper():

                score = int(
                    ''.join(
                        filter(str.isdigit, line)
                    )
                )

                break

    except:

        score = 0

    # ==================================
    # SALVA PERFORMANCE
    # ==================================

    save_performance(
        topic,
        score
    )

    return evaluation