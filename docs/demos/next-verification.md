# Next: complete input-to-answer demonstrations

InterviewForge now has a completed real model-answer demonstration. AgentForge retains its actual MCP/file recording while Claude generation awaits the backend credential.

## InterviewForge: completed PDF-to-answer flow

The original UI now demonstrates real Llama 3.2 generation with expanded PDF sources. A separate unsupported salary question was correctly declined. See the [recording and reproduction notes](./interviewforge.md) and [actual response](./interviewforge-live-result.json).

Next, verify a complete five-question mock interview, scoring and adaptive follow-ups. Those flows remain unverified.

## AgentForge: Claude response pending secret configuration

The owner chose to keep Claude. Configure `ANTHROPIC_API_KEY` in backend secret settings; do not paste it into chat or commit it. No local-provider substitution was made.

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
