# InterviewForge: real PDF-to-answer demonstration

The original React UI uploads a public PDF, retrieves passages from ChromaDB, and receives a real **Llama 3.2** answer through Ollama. The recording ends with the source passage expanded. No responses were mocked.

![Actual PDF upload, model answer and expanded source](../../assets/demos/interviewforge-live-recording.gif)

[Full-resolution screenshot](../../assets/projects/interviewforge-live-answer.png) · [Captured response and checks](./interviewforge-live-result.json) · [Project source](https://github.com/Sumanthduasanapudi/InterviewForge-AI)

## Verified behavior

Question: **Which database and local language model does InterviewForge AI use? Answer briefly using the uploaded notes.**

Actual answer:

> InterviewForge AI uses ChromaDB as its vector database and serves its local large language model, Llama 3.2, through Ollama.

The answer matches the uploaded [public technical notes](./InterviewForge_RAG_Demo.pdf). The response included three source chunks: one from that document and two from [Public_Project_Notes.pdf](./Public_Project_Notes.pdf). The UI displayed the answer and expanded the relevant source. Browser page errors: **0**.

A separate real API request asked for the developer’s salary, which is absent from the notes. The model answered:

> I couldn't find any information about the developer salary in Indian rupees in the uploaded notes.

[Unsupported-question response](./interviewforge-unsupported-response.json). These two cases demonstrate this captured run, not a general accuracy benchmark.

## Runtime and scope

- Unmodified project checkout: [`f99f70dc73799937cb3e6173cbe73cd8f3e34273`](https://github.com/Sumanthduasanapudi/InterviewForge-AI/tree/f99f70dc73799937cb3e6173cbe73cd8f3e34273).
- Original React frontend → FastAPI `/ask` → ChromaDB retrieval → Ollama → visible answer and sources.
- Python 3.12, FastAPI 0.141.1, ChromaDB 1.5.9 and PyPDF 6.10.0.
- Ollama 0.40.15, `llama3.2:3b`, 3.2B parameters, Q4_K_M quantization, 4096-token context, CPU execution.
- Model digest: `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`.
- Two public sample documents, three indexed chunks. No private résumé or credentials in this demonstration.

This is a recorded local demonstration, not a hosted LLM service. Mock-interview scoring and adaptive follow-up sessions have not been verified here.

## Reproduce locally

Install Python 3.12+, Node.js, npm and Ollama. Start Ollama with `ollama serve`, then in another terminal:

```bash
ollama pull llama3.2:3b
```

In the InterviewForge source checkout:

```bash
python -m venv .venv
# Activate the virtual environment for your operating system.
python -m pip install -r requirements.txt
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

In another terminal:

```bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1 --port 5173
```

Open `http://127.0.0.1:5173`, upload the public technical notes linked above, ask the recorded question and expand the source. ChromaDB downloads its embedding model on first use. Use one backend process per ChromaDB directory.

For an additional real API capture, run from the profile checkout:

```bash
python docs/demos/check_live_flow.py interviewforge --output interviewforge-live-result.json
```

Review the answer against the source; a successful HTTP response alone does not establish correctness.
