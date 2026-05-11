# AI Newsletter Agent

An autonomous AI agent that researches, summarizes, reviews, and generates newsletters automatically.

## Features

- Autonomous AI workflow
- Human-in-the-loop approval mode
- AI-powered article summarization
- Newsletter HTML generation
- Downloadable newsletter
- Live workflow visualization
- Local LLM support using Ollama

## Workflow

1. Planning
2. Research
3. Summarization
4. Human Approval (Optional)
5. Newsletter Generation
6. Download

## Tech Stack

- Python
- Streamlit
- Ollama
- LangChain
- Tavily Search API

## Run Locally

### Activate Environment

```bash
source venv/bin/activate
```

### Run Ollama

```bash
ollama run llama3
```

### Start App

```bash
streamlit run app.py
```

## Example Goal

```txt
Create a weekly newsletter on latest AI agent news
```

## Project Structure

```txt
newsletter/
│
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── README.md
└── venv/
```

## Assignment Requirements Covered

- Autonomous AI Agent
- Multi-step reasoning
- Tool usage
- Human-in-the-loop mode
- Self-reflection workflow
- Newsletter generation
- Frontend interface