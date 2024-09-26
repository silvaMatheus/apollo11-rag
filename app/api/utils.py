import os
from app.core.config import DATA_DIR

def get_all_file_names():
    all_file_names = []
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if not file.startswith('.'):
                all_file_names.append(os.path.join(root, file))
    return all_file_names