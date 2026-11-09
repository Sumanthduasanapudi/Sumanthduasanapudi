# Fixed evaluation plan

Defined before running the eight RAG requests. The question list and expected facts are in `evaluate_rag.py`. The backend, prompt and model are unchanged.

- Six answerable questions: database, model/server, backend stack, retrieval count, practice length and score range.
- Two unsupported questions: developer salary and production employer.
- Report fact checks separately from refusal checks. Inspect complete answers for contradictions beyond the required terms.
- Retrieval: rank of the known relevant technical-notes chunk, top-1 hit rate and mean reciprocal rank, on answerable questions only.
- Corpus is two short public PDFs, three chunks total. Top-3 retrieval includes the entire corpus and is not a useful quality metric. This is a smoke evaluation, not a held-out retrieval benchmark.
- Latency is client-observed `perf_counter` time for the original `/ask` endpoint, including retrieval and full non-streaming generation; serial requests, one run per question, warm model after mock-interview use. Report median, mean, range and nearest-rank p95; with n=8 p95 equals maximum and is unstable.
- Mock-interview scores are model opinions about explicitly scripted demo answers. Verify score fields in 0–10, nonempty feedback/improved answer, four next questions, no sixth question, and UI completion with average. Do not treat model scores as grading accuracy.
