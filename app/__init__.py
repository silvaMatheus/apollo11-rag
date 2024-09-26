from .api import get_all_file_names
from .core import GOOGLE_API_KEY, DATA_DIR, MODEL_NAME, EMBEDDING_MODEL
from .services import process_all_data, create_rag_system, query_rag

__all__ = [
    'get_all_file_names',
    'GOOGLE_API_KEY',
    'DATA_DIR',
    'MODEL_NAME',
    'EMBEDDING_MODEL',
    'process_all_data',
    'create_rag_system',
    'query_rag'
]

 
print("Inicializando o pacote app...")