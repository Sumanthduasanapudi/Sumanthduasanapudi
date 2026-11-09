"""Run the original AgentForge MCP routes for a local, read-only demonstration.
Usage: python agentforge_mcp_runner.py /path/to/AgentForge
This does not simulate or enable Claude/CrewAI/RAG model responses.
"""
import shutil
import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI
root=Path(sys.argv[1]).resolve()
if not (root/'backend/mcp_api.py').is_file():
    raise SystemExit('Pass the AgentForge checkout directory.')
sys.path.insert(0,str(root/'backend'))
from mcp_api import router
workspace=root/'mcp_workspace'
workspace.mkdir(exist_ok=True)
if not (workspace/'project_notes.txt').exists():
    shutil.copyfile(Path(__file__).with_name('project_notes.txt'),workspace/'project_notes.txt')
app=FastAPI(title='AgentForge read-only MCP demonstration')
app.include_router(router)
@app.get('/api/health')
def health():
    return {'status':'online','scope':'MCP-only','llm_configured':False}
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
