# InterviewForge: recorded PDF-ingestion workflow

This recording uses the actual React frontend and original FastAPI application. It shows a public sample PDF being indexed into the Knowledge Vault, followed by the application's mock-interview and Python-study **setup screens**. No interview is started and no generated model response is simulated.

![Recorded PDF upload and practice setup screens](../../assets/demos/interviewforge-recording.gif)

[Full-resolution screenshot](../../assets/projects/interviewforge-vault.png) · [Project source](https://github.com/Sumanthduasanapudi/InterviewForge-AI)

## What ran

- Source checkout: [`f99f70dc73799937cb3e6173cbe73cd8f3e34273`](https://github.com/Sumanthduasanapudi/InterviewForge-AI/tree/f99f70dc73799937cb3e6173cbe73cd8f3e34273).
- Original frontend and `api.py`; no frontend API responses were mocked.
- [Public sample PDF](./Public_Project_Notes.pdf) uploaded through the UI and indexed as **2 chunks** in persistent ChromaDB.
- A separate **same-process ingestion and retrieval check** used the original `add_pdf_to_vault` and `retrieve_context` helpers. It returned source text, filenames, chunk metadata and distances for both available chunks. [See the captured retrieval result](./interviewforge-retrieval.json).
- Browser page errors in the captured UI flow: **0**.

The sample contains public project descriptions, not the candidate's private résumé. The application retrieves up to three chunks; this short sample has only two, so the check returned two.

## Reproduce locally

Requires Python 3.12+, Node.js and npm. In the InterviewForge checkout:

```bash
python -m venv .venv
# Activate the virtual environment for your operating system.
python -m pip install -r requirements.txt
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

In a second terminal:

```bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1 --port 5173
```

Open `http://127.0.0.1:5173` and upload [Public_Project_Notes.pdf](./Public_Project_Notes.pdf). ChromaDB may download its default embedding model on first use. The captured run used ChromaDB **1.5.9**, PyPDF **6.10.0**, FastAPI **0.141.1**, and Python **3.12**.

For the separate retrieval check, first stop the API server, activate the same Python environment, and run this from the profile checkout:

```bash
python docs/demos/verify_interviewforge.py ../InterviewForge-AI
```

Use one backend process per ChromaDB directory. The separate check ingests and queries through the same process to avoid stale cross-process state.

## Model-generation prerequisite

The screenshot's `llama3.2:3b` label is the **configured model name**, not proof that Ollama is running. To test generated answers locally, install Ollama, run `ollama serve`, and pull `llama3.2:3b`. A completed Llama answer, scoring session and adaptive next question were **not verified in this recording**.

This is a recorded local demonstration, not a hosted LLM service.
