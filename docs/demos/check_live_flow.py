"""Capture an actual backend response; never simulate model output.
Run only against your own configured local application.
"""
import argparse,json,sys,urllib.request,urllib.error
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('project',choices=['agentforge','interviewforge'])
p.add_argument('--base-url',default='http://127.0.0.1:8000')
p.add_argument('--output',type=Path,default=Path('live-flow-result.json'))
a=p.parse_args();base=a.base_url.rstrip('/')
def request(path,body=None):
    r=urllib.request.Request(base+path,data=None if body is None else json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(r,timeout=180) as response:return json.load(response)
try:
    if a.project=='agentforge':
        health=request('/api/health')
        if not health.get('api_key_configured'):raise RuntimeError('Start the full AgentForge backend with a working Claude API configuration; the MCP-only runner is insufficient.')
        payload={'mode':'general','messages':[{'role':'user','content':'In two sentences, explain why a RAG application should show the source passages used for an answer.'}]}
        result=request('/api/chat',payload)
        answer=result.get('reply','')
    else:
        health=request('/health')
        if not health.get('chunks'):raise RuntimeError('Upload Public_Project_Notes.pdf through the application before testing.')
        payload={'question':'Which database and local language model does InterviewForge use? Cite the uploaded public project notes.'}
        result=request('/ask',payload)
        answer=result.get('answer','')
        if not result.get('sources'):raise RuntimeError('No source passages were returned; this is not evidence of a completed retrieval flow.')
    if not isinstance(answer,str) or not answer.strip() or answer.lstrip().upper().startswith('ERROR'):raise RuntimeError('The backend did not return a usable model answer.')
    a.output.write_text(json.dumps({'project':a.project,'request':payload,'response':result,'checks':{'nonempty_answer':True,'human_factual_review_required':True}},indent=2))
    print(f'Captured actual backend output in {a.output}. Review factual accuracy before publishing.')
except (urllib.error.URLError,TimeoutError,RuntimeError,ValueError) as error:
    print(f'NOT VERIFIED: {error}',file=sys.stderr);sys.exit(1)
