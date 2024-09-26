import google.generativeai as genai
from app.core.config import GOOGLE_API_KEY
from app.services import process_all_data, create_rag_system, query_rag
from app.api.utils import get_all_file_names

def main():
    genai.configure(api_key=GOOGLE_API_KEY)
    
    print("Processing data...")
    all_files, all_summaries = process_all_data()
    
    print("Creating RAG system...")
    db = create_rag_system(all_summaries)
    
    all_file_names = get_all_file_names()
    
    print("RAG system ready for queries!")
    while True:
        query = input("Enter your query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        
        response, used_files = query_rag(query, db, all_files, all_file_names)
        print("\nResponse:", response)
        print("\nUsed files:", used_files)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()