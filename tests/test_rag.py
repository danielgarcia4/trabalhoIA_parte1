from src.rag.chunking import chunk_text

def test_chunking():

    text = "a" * 2000

    chunks = chunk_text(text)

    assert len(chunks) > 1