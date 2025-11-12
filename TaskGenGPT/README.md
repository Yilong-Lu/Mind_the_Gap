# TaskGenGPT


## `.env`

```
AI_OAI_API_KEY= # your key
AI_API_VERSION=2024-09-01-preview
AI_API_BASE= # your api

# optional, for langsmith tracing
# https://smith.langchain.com/
LANGCHAIN_PROJECT=...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=...
```


## Codes
`agents` folder contains the codes for task generation

`TaskGenGPT/agents/naive_agent.py` contains the simple llm model.

`TaskGenGPT/agents/reflexion_agent.py` contains the llm model with reflexion.

`TaskGenGPT/agents/roleplay_agent.py` complete the task generation experiment with real individual information collected from human experiments.

`prompts` folder contains the task prompts.