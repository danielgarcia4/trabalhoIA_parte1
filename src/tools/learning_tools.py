from src.rag.retriever import retrieve
from src.llm.client import ask_llm

def gerar_exercicios(topic):

    docs = retrieve(topic)

    context = "\n".join(docs)

    prompt = f"""
    Baseado no contexto abaixo:

    {context}

    Gere:
    - 5 exercícios
    - dificuldade média
    - respostas no final
    """

    return ask_llm(prompt)