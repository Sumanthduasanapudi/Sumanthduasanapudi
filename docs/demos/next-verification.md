# Next: complete input-to-answer demonstrations

The existing recordings show actual MCP/file operations and document ingestion. These are the remaining steps for demonstrating model output. They have not been completed in the published evidence.

## InterviewForge: local, no provider API key

1. Install Ollama, start it with `ollama serve`, and run `ollama pull llama3.2:3b`.
2. Start the original InterviewForge API and frontend using the [recorded-demo instructions](./interviewforge.md).
3. Upload the supplied [public project notes](./Public_Project_Notes.pdf).
4. Ask: **Which database and local language model does InterviewForge use?**
5. Show the answer and expand the returned sources. Compare its claims with the uploaded text.

To capture a real response as JSON, run from the profile checkout:

```bash
python docs/demos/check_live_flow.py interviewforge --output interviewforge-live-result.json
```

The check requires non-empty model output and returned source passages. It does not certify factual correctness; a person must review the answer.

## AgentForge: actual Claude response

1. Run the full backend with your own working Claude configuration. The MCP-only runner does not generate AI answers.
2. Keep the key in the backend environment. Never place it in the browser or repository.
3. Use the normal chat or documented retrieval workflow, showing the submitted question and complete response.
4. For a retrieval demonstration, also show the uploaded public document and the passages used by the answer.

A minimal real-chat check, using the existing backend's configured provider, is:

```bash
python docs/demos/check_live_flow.py agentforge --output agentforge-live-result.json
```

This makes one real Claude request and can consume provider credits. The check captures a chat response only; it does not certify a full multi-agent or RAG workflow.

## Publish only after checking

Record the actual UI flow, review the answer against the source, and then replace the current limited-scope recording. Do not use fixture responses as proof of live model generation. Keep private documents and credentials out of recordings and result files.

## Profile asset check

```bash
python scripts/check_readme.py
```

This checks local assets and README section anchors. External service availability and browser rendering require separate checks.
