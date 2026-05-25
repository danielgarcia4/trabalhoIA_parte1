from src.tools.active_recall import gerar_pergunta

def test_gerar_pergunta():

    pergunta = gerar_pergunta(
        "RAG"
    )

    assert pergunta is not None