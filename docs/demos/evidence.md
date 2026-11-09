# Project evidence and capture scope

These screenshots are actual browser captures of the project interfaces, not generated mockups.

| Project | Captured evidence | Important limit |
| --- | --- | --- |
| AgentForge | Original frontend and real read-only MCP server: discovery, file reading and search | A minimal MCP-only FastAPI runner was used; model-based answers were not tested |
| InterviewForge | Original UI/API: PDF upload, ChromaDB retrieval, actual Llama 3.2 answer and expanded sources | Five-question scoring flow also completed; grading inconsistencies and repeated follow-ups documented in the [evaluation](./interviewforge-evaluation.md) |
| NewsPulse | Original frontend and Express gateway with the repository's real RSS collector | A read-only FastAPI runner exposed collection and the repository's saved example stories; Claude briefings were not generated |
| Meeting Minutes | User-provided public demo at https://ai-meeting-summary-dun.vercel.app/ rendered its upload/agenda/attendee/PIN interface | Page loading was checked; no transcript was submitted and no protected summarization call was tested |

NewsPulse source: [`8b1285737eadc701a8b369ab0823f88e2c6c5ee1`](https://github.com/Sumanthduasanapudi/newspulse-ai/tree/8b1285737eadc701a8b369ab0823f88e2c6c5ee1). Its RSS collector returned live article metadata. Stored example stories in that repository are sample content, not verified current events or outputs generated in this capture.

The recordings cover the specific flows listed above. They do not establish complete production readiness, model accuracy, security guarantees, or the status of every external provider.
