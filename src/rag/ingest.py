from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import os

from src.rag.chunking import chunk_text

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="materiais"
)

def load_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text

def ingest_pdf(path):

    filename = os.path.basename(path)

    text = load_pdf(path)

    chunks = chunk_text(text)

    embeddings = model.encode(chunks).tolist()

    ids = [
        f"{filename}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {"source": filename}
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return f"{len(chunks)} chunks indexados."