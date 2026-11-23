# Python AI Journey 🐍🤖

My hands-on path from zero Python to building production-style AI applications: LLM apps, RAG, agents and MCP servers.


---

## 🎯 Goals

- Write idiomatic, typed, tested Python
- Analyze data with NumPy and Pandas
- Build REST APIs with FastAPI (and connect them to Angular)
- Build LLM-powered applications: chat, structured output, RAG, tool calling, agents and MCP
- Finish at least two portfolio-ready capstone projects

---

## 🛠️ Tech stack

| Area | Tools |
| --- | --- |
| Language | Python 3.13 |
| Package / env manager | [uv](https://docs.astral.sh/uv/) |
| Editor | VS Code (Python, Pylance, Jupyter, Ruff extensions) |
| Quality | Ruff (lint + format), mypy (types), pytest (tests) |
| Data | NumPy, Pandas, Matplotlib, SQLAlchemy |
| Backend | FastAPI, Pydantic, SQLModel, Docker |
| AI | Anthropic / OpenAI SDKs, ChromaDB, sentence-transformers, MCP |

---

## 🚀 Getting started

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- Git
- VS Code (recommended)

### Setup

```bash
git clone https://github.com/<your-username>/python-ai-journey.git
cd python-ai-journey
uv sync                 # creates .venv and installs all dependencies
```

In VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → choose `.venv`.

### Environment variables

Create a `.env` file in the project root (it is git-ignored):

```env
ANTHROPIC_API_KEY=your-key-here
OPENAI_API_KEY=your-key-here
```

> ⚠️ Never commit API keys. Keep a `.env.example` with empty values instead.

---

## ▶️ Running code

```bash
uv run python-ai-journey              # run the package entry point (src/)
uv run module1_core/hello.py          # run any single practice file
uv run pytest                         # run all tests
uv run ruff check .                   # lint
uv run ruff format .                  # format
uv run mypy .                         # type-check
```

Or open a `.py` file in VS Code and press **▷** (run) or **F5** (debug).

---

## 📁 Project structure

```text
python-ai-journey/
├── src/python_ai_journey/   # package entry point / reusable code
├── module1_core/            # Core Python: syntax, collections, classes, files
├── module2_pythonic/        # Type hints, generators, decorators, async, Pydantic
├── module3_data/            # NumPy, Pandas, charts, APIs, SQLAlchemy
├── module4_fastapi/         # FastAPI CRUD APIs, auth, Docker
├── module5_ai/              # LLM calls, structured output, RAG, agents, MCP
├── capstones/               # Portfolio projects
├── tests/                   # pytest tests
├── pyproject.toml           # project config & dependencies
├── uv.lock                  # locked dependency versions
└── README.md
```

---

## 📚 Learning roadmap & progress

| Week | Module | Topics | Status |
| --- | --- | --- | --- |
| 1–2 | **1. Core Python** | Syntax, collections, comprehensions, functions, classes, dataclasses, exceptions, files, JSON | ⬜ |
| 3–4 | **2. Pythonic Python** | Type hints, generators, decorators, async/await, Pydantic, pytest | ⬜ |
| 5–6 | **3. Data handling** | NumPy, Pandas (SQL → Pandas), Matplotlib, httpx, SQLAlchemy | ⬜ |
| 7–8 | **4. FastAPI backends** | CRUD APIs, dependency injection, Angular integration, JWT auth, Docker | ⬜ |
| 9–12 | **5. AI development** | LLM APIs, streaming, prompt engineering, embeddings, RAG, tool calling, agents, MCP, evals | ⬜ |

Status key: ⬜ not started · 🟨 in progress · ✅ done

### Practice exercises

<details>
<summary><b>Module 1: Core Python</b></summary>

- [ ] FizzBuzz variants
- [ ] Word counter
- [ ] Student grades
- [ ] Bank account system
- [ ] Contact book CLI
- [ ] Log file analyzer

</details>

<details>
<summary><b>Module 2: Pythonic Python</b></summary>

- [ ] Add type hints (`mypy --strict` passes)
- [ ] Retry decorator
- [ ] Lazy file pipeline (generators)
- [ ] Concurrent downloader (asyncio + httpx)
- [ ] Config loader (pydantic-settings)
- [ ] Tests with 80%+ coverage

</details>

<details>
<summary><b>Module 3: Data handling</b></summary>

- [ ] NumPy drills
- [ ] Rewrite 5 SQL queries in Pandas
- [ ] Sales analysis notebook
- [ ] API → database with SQLAlchemy
- [ ] Similarity search from scratch

</details>

<details>
<summary><b>Module 4: FastAPI backends</b></summary>

- [ ] Hello API
- [ ] Persistent Tasks API (SQLModel)
- [ ] Angular + FastAPI integration
- [ ] API tests with TestClient
- [ ] JWT auth + Docker Compose

</details>

<details>
<summary><b>Module 5: AI development</b></summary>

- [ ] CLI chatbot with streaming
- [ ] Prompt lab
- [ ] CV parser (structured output)
- [ ] Document Q&A (RAG) API
- [ ] SQL agent (tool calling)
- [ ] Tasks MCP server
- [ ] RAG evaluation

</details>

---

## 🏆 Capstone projects

| Project | Description | Status |
| --- | --- | --- |
| **A. Knowledge assistant (RAG)** | Chat over company documents with citations: Angular → FastAPI → Claude + pgvector | ⬜ |
| **B. Natural-language SQL analyst** | Ask business questions in plain English; get answers and charts | ⬜ |
| **C. MCP server** | Expose a real system as tools for AI assistants | ⬜ |
| **D. Document processing pipeline** | Extract structured data from invoices / CVs with accuracy tracking | ⬜ |


---

## 🔗 Resources

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Pandas: comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Claude API docs](https://docs.claude.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Exercism Python track](https://exercism.org/tracks/python)

---

*Started: November 2026*