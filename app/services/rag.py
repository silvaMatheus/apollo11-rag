import logging
from typing import List, Tuple
from app.services.embedding import create_chroma_db
from app.core.config import MODEL_NAME
import google.generativeai as genai

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

model = genai.GenerativeModel(MODEL_NAME, )

def get_relevant_files(query: str, db) -> List[str]:
    results = db.query(query_texts=[query], n_results=3)
    return results["ids"][0]

def query_rag(query: str, db, all_files: List[str], all_file_names: List[str]) -> Tuple[str, List[str]]:
    files = get_relevant_files(query, db)
    prompt = [all_files[int(f)] for f in files]
    prompt.append("Generate a response to the query using the provided files. Here is the query:")
    prompt.append(query)
    response = model.generate_content(prompt).text
    used_files = [all_file_names[int(f)] for f in files]
    return response, used_files

def create_rag_system(all_summaries: List[str]):
    logging.info(f"Creating RAG system with {len(all_summaries)} summaries")
    db = create_chroma_db(all_summaries, "nasa")
    logging.info("RAG system created")
    return db