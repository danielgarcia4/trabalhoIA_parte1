from src.tools.learning_tools import gerar_exercicios

def test_gerar_exercicios():

    result = gerar_exercicios(
        "embeddings"
    )

    assert result is not None