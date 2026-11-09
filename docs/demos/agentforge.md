# AgentForge: recorded read-only MCP workflow

This is a recording of the actual React application connected to the original FastAPI MCP routes and stdio MCP server. It demonstrates tool discovery, reading a public sample file, and searching for `LangGraph`. No Claude, CrewAI, or RAG model response is simulated or claimed.

![Recorded MCP discovery, file reading and search](../../assets/demos/agentforge-recording.gif)

[Full-resolution screenshot](../../assets/projects/agentforge-mcp.png) · [Project source](https://github.com/Sumanthduasanapudi/AgentForge)

## What ran

- Source checkout: [`0c31e8deb3684c68952b4b0dfc7e896b3ad155a1`](https://github.com/Sumanthduasanapudi/AgentForge/tree/0c31e8deb3684c68952b4b0dfc7e896b3ad155a1).
- Unmodified React frontend from that checkout.
- Original `backend/mcp_api.py` and `backend/mcp_server.py`, mounted in a small **MCP-only runner**. This is narrower than the complete application's model-dependent backend.
- Three tools discovered: `list_workspace_files`, `read_workspace_file`, `search_workspace`.
- `project_notes.txt` was read successfully; searching `LangGraph` returned a source line from that file.
- Browser page errors in this captured flow: **0**.

The sample file contains public project notes. It contains no credentials or private candidate data. The frontend's “AI System Active” and backend-online indicators describe the running interface/backend; they do not establish that Claude or CrewAI is configured.

## Reproduce locally

Requires Python 3.12+, Node.js and npm. Clone this profile repository alongside the AgentForge repository, then from the profile checkout:

```bash
python -m venv .venv
# Activate the virtual environment for your operating system.
python -m pip install fastapi uvicorn 'mcp>=1,<2'
python docs/demos/agentforge_mcp_runner.py ../AgentForge
```

In a second terminal:

```bash
cd ../AgentForge/frontend
npm ci
npm run dev
```

Open `http://127.0.0.1:5174`, select **MCP Tool Center**, then try **Read File** and **Search Files**. The sample runner uses port 8000. Stop it before running the separate InterviewForge demonstration.

The runner adds the supplied public notes only if `project_notes.txt` does not already exist. Existing workspaces may therefore produce different text. No application source files are modified by the runner.

## Scope

This is a **recorded local demonstration**, not a hosted, always-on AgentForge service. Live model generation, paid-provider availability and full multi-agent completion are not verified by this recording.
