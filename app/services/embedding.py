import google.generativeai as genai
from chromadb import Documents, EmbeddingFunction, Embeddings
from app.core.config import EMBEDDING_MODEL

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        title = "Custom query"
        return genai.embed_content(model=EMBEDDING_MODEL,
                                   content=input,
                                   task_type="retrieval_document",
                                   title=title)["embedding"]

def create_chroma_db(documents, name):
    import chromadb
    chroma_client = chromadb.Client()
    db = chroma_client.get_or_create_collection(name=name, embedding_function=GeminiEmbeddingFunction())
    
    for i, d in enumerate(documents):
        db.add(
            documents=d,
            ids=str(i)
        )
    return db