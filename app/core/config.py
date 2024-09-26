import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'app/resources')
 
 
MODEL_NAME = 'models/gemini-1.5-flash'
EMBEDDING_MODEL = 'models/text-embedding-004'