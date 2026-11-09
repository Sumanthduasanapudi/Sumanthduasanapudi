"""Real PDF ingestion/retrieval check using the original InterviewForge helpers.
Stop the local API server before running this separate ChromaDB process.
Usage: python verify_interviewforge.py /path/to/InterviewForge-AI
"""
import json
import shutil
import sys
from pathlib import Path
root=Path(sys.argv[1]).resolve()
if not (root/'api.py').is_file():
    raise SystemExit('Pass the InterviewForge-AI checkout directory.')
sys.path.insert(0,str(root))
import api
sample=Path(__file__).with_name('Public_Project_Notes.pdf')
destination=api.DOCUMENTS_FOLDER/sample.name
shutil.copyfile(sample,destination)
ingestion=api.add_pdf_to_vault(destination)
query='Which components does InterviewForge use for document retrieval?'
documents,metadatas,distances=api.retrieve_context(query)
assert documents and all(documents),'Missing source text'
assert metadatas and all(metadatas),'Missing source metadata'
print(json.dumps({'ingestion':ingestion,'query':query,'sources':[{'text':text,'metadata':meta,'distance':distance} for text,meta,distance in zip(documents,metadatas,distances)],'llm_generation_verified':False},indent=2))
