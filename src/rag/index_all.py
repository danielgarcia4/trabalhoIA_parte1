import os

from src.rag.ingest import ingest_pdf

PDF_FOLDER = "data/pdfs"

def index_all_pdfs():

    files = os.listdir(PDF_FOLDER)

    pdfs = [
        file
        for file in files
        if file.endswith(".pdf")
    ]

    if not pdfs:
        print("Nenhum PDF encontrado.")
        return

    for pdf in pdfs:

        path = os.path.join(
            PDF_FOLDER,
            pdf
        )

        print(f"Indexando: {pdf}")

        result = ingest_pdf(path)

        print(result)

if __name__ == "__main__":

    index_all_pdfs()