import pathlib
from PIL import Image
import pytesseract
import google.generativeai as genai
from app.core.config import DATA_DIR, MODEL_NAME

model = genai.GenerativeModel(MODEL_NAME)

def create_summary(modality):
    path = pathlib.Path(DATA_DIR) / modality

    summary_prompt = f"""You are an assistant tailored for summarizing {modality} for the Apollo 11 mission.
    These summaries will be turned into vector embeddings and used to retrieve the most relevant information.
    Give a concise summary of the {modality} that is well optimized for retrieval. Here is the {modality}:"""

    files = []
    summaries = []
    
    for f in path.glob("*"):
        print(f"File: {f}")
        if f.is_dir() or f.name.startswith('.'):
            continue
        print(f"Processing: {f}")
        
        if modality == "text":
            file = Image.open(f)
            response = model.generate_content([summary_prompt, pytesseract.image_to_string(file)])
       
        else:
            file = genai.upload_file(f)

            while file.state.name == "PROCESSING":
                print("Waiting for video file upload...\n", end='')
                file = genai.get_file(file.name)

            response = model.generate_content([summary_prompt, file])

        files.append(file)
        summaries.append(response.text)

    return files, summaries

def process_all_data():
    all_files = []
    all_summaries = []
    for modality_type in ["audio", "text", "video"]:
        files, summaries = create_summary(modality_type)
        all_files.extend(files)
        all_summaries.extend(summaries)
    return all_files, all_summaries