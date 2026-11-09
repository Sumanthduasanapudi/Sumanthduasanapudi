"""Small, fixed public-document smoke evaluation; no provider credentials required."""
import json,time,urllib.request,statistics,platform,datetime
from pathlib import Path
CASES=[
 {'id':'database','question':'Which vector database does InterviewForge AI use? Answer in one sentence.','required':['chromadb'],'answerable':True},
 {'id':'model','question':'Which local language model and serving tool does InterviewForge AI use? Answer briefly.','required':['llama','3.2','ollama'],'answerable':True},
 {'id':'backend','question':'What backend language and framework does InterviewForge AI use? Answer briefly.','required':['python','fastapi'],'answerable':True},
 {'id':'retrieval','question':'What is the maximum number of source chunks retrieved for each InterviewForge question? Answer briefly.','required_any':[['three','3']],'answerable':True},
 {'id':'session','question':'How many questions are in an InterviewForge practice session? Answer briefly.','required_any':[['five','5']],'answerable':True},
 {'id':'scores','question':'What score range do InterviewForge practice sessions use? Answer briefly.','required':['0','10'],'answerable':True},
 {'id':'salary','question':'What is the developer salary in Indian rupees? Answer only if stated in the uploaded notes.','answerable':False},
 {'id':'employer','question':'Which employer deployed InterviewForge in production? Answer only if stated in the uploaded notes.','answerable':False},
]
def main():
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--base-url',default='http://127.0.0.1:8000');ap.add_argument('--output',default='rag-evaluation.json');a=ap.parse_args()
 result={'runtime':{'model':'llama3.2:3b','quantization':'Q4_K_M','context_tokens':4096,'ollama_version':'0.40.15','hardware':'CPU only; 3 vCPUs, Intel Xeon Platinum 8573C; 9.7 GiB host RAM','project_commit':'f99f70dc73799937cb3e6173cbe73cd8f3e34273'},'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Eight fixed questions, one run each, serial requests, original /ask endpoint, time.perf_counter end-to-end HTTP latency; source retrieval included. Model already warm after mock interview.','corpus':'Two public PDFs, three total chunks; all six answerable questions target InterviewForge_RAG_Demo.pdf chunk 0. Top-3 recall is trivial for this corpus, so only focused-source rank and top-1 hit are reported.','cases':[]}
 for case in CASES:
  t=time.perf_counter()
  req=urllib.request.Request(a.base_url+'/ask',data=json.dumps({'question':case['question']}).encode(),headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=240) as r:response=json.load(r)
  elapsed=time.perf_counter()-t;answer=response['answer'].lower()
  rank=next((i for i,s in enumerate(response['sources'],1) if s['source']=='InterviewForge_RAG_Demo.pdf' and s['chunk']==0),None)
  passed=(all(x in answer for x in case.get('required',[])) and all(any(x in answer for x in group) for group in case.get('required_any',[]))) if case['answerable'] else any(x in answer for x in ["couldn't find","not mentioned","not provided","not specified","does not mention","don't have","no information","not stated","no employer","not documented","does not provide","do not contain"])
  result['cases'].append({**case,'response':response,'elapsed_seconds':round(elapsed,3),'focused_source_rank':rank,'automatic_check_passed':passed})
  Path(a.output).write_text(json.dumps(result,indent=2));print(case['id'],round(elapsed,2),passed,rank,flush=True)
 times=sorted(c['elapsed_seconds'] for c in result['cases']);ans=[c for c in result['cases'] if c['answerable']];neg=[c for c in result['cases'] if not c['answerable']]
 result['summary']={'answerable_fact_checks_passed':sum(c['automatic_check_passed'] for c in ans),'answerable_cases':len(ans),'abstention_checks_passed':sum(c['automatic_check_passed'] for c in neg),'unanswerable_cases':len(neg),'focused_source_top1_hits':sum(c['focused_source_rank']==1 for c in ans),'focused_source_mrr':sum(1/c['focused_source_rank'] if c['focused_source_rank'] else 0 for c in ans)/len(ans),'latency_seconds':{'median':statistics.median(times),'mean':statistics.mean(times),'min':min(times),'max':max(times),'p95_nearest_rank':times[-1]},'runs_per_case':1}
 Path(a.output).write_text(json.dumps(result,indent=2));print(json.dumps(result['summary']),flush=True)
if __name__=='__main__':main()
