from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_collection(
    "materiais"
)

def retrieve(query, k=5):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    documents = results["documents"][0]

    print("\nDOCUMENTOS RECUPERADOS:\n")

    for doc in documents:

        print(doc[:300])

        print("\n====================\n")

    return documents