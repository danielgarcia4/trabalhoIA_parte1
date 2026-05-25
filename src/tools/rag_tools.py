from src.rag.retriever import retrieve
from src.llm.client import ask_llm
from src.utils.logger import logger

def buscar_material_rag(question):

    docs = retrieve(question)

    if not docs:

        return "Nenhum conteúdo encontrado."

    context = "\n\n".join(docs)

    prompt = f"""
    Você é um assistente acadêmico.

    Use o contexto abaixo para responder a pergunta.

    Caso a informação esteja parcialmente presente,
    tente responder da melhor forma possível.

    Contexto:
    {context}

    Pergunta:
    {question}

    Resposta:
    """

    answer = ask_llm(prompt)

    logger.info(f"""
    TOOL: buscar_material_rag
    INPUT: {question}

    CONTEXT:
    {context}

    OUTPUT:
    {answer}
    """)

    return answer