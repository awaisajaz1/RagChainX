# RAG Learning with Local Ollama and SQL

## Project Overview
This project demonstrates how to build a Retrieval-Augmented Generation (RAG) system using local Large Language Models (LLMs) via Ollama and interacting with a SQL database using LangChain. It shows how to query a database using natural language and an LLM.

## Quick Start
Follow these steps to get the project running locally.

### 1. Environment Setup

**Prerequisites:**
- Python 3.12+
- [Ollama](https://ollama.ai/) installed (see guide below)

**Clone and Install:**
```bash
# Clone the repository (if you haven't already)
# git clone <repo-url>
# cd rag-learning

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirments.txt
```

### 2. Database Setup
The project uses a local SQLite database (`demo.db`). A script is provided to generate this database with sample data.

```bash
# Run the database generation script
python demo_db.py
```
This will create `demo.db` with `customers` and `Sales` tables.

### 3. Ollama Setup
This project uses `llama3`. Ensure you have Ollama installed and pull the model:

```bash
# Start Ollama server (in a separate terminal)
ollama serve

# Pull the model
ollama pull llama3
```

## Usage

### Running the Notebook
The main logic is in the Jupyter Notebook `rager_the_smasher.ipynb`.

1.  Ensure your virtual environment is activated.
2.  Start Jupyter:
    ```bash
    jupyter notebook
    ```
3.  Open `rager_the_smasher.ipynb`.
4.  Run the cells to see the RAG agent in action querying the `demo.db`.

---

# Ollama – Complete Installation Guide

Ollama lets you run large language models **locally** on your machine. No API keys, no internet required after download.

---

## What is Ollama?

* A local AI runtime for LLMs (LLaMA, Mistral, Phi, etc.)
* Runs fully on your laptop (CPU / Apple Silicon)
* Exposes a local HTTP API (default: `http://localhost:11434`)
* Works with tools like **LangChain**, **LlamaIndex**, **CrewAI**

---

## System Requirements

* macOS (Apple Silicon recommended)
* Linux (x86_64 / ARM)
* Windows (via WSL)
* Disk space: **~5–10 GB** recommended
* RAM: **8 GB minimum**, **16 GB recommended**

---

## Installation

### macOS (Homebrew – CLI)

```bash
brew install ollama
```

Verify:

```bash
ollama --version
```

---

## Starting Ollama

### Start server (CLI-only install)

```bash
ollama serve
```

* Keep this terminal **open**
* Ollama listens on port **11434**

Verify in another terminal:

```bash
curl http://localhost:11434
```

Expected:

```
Ollama is running
```

---

## Downloading Models

### Pull a model

```bash
ollama pull mistral
```

Popular models:

| Model   | Size    | Notes              |
| ------- | ------- | ------------------ |
| mistral | ~4 GB   | Fast, good default |
| llama3  | ~5 GB   | Better reasoning   |
| phi     | ~1.6 GB | Very lightweight   |

Models are stored in:

```text
~/.ollama
```

---

## Running a Model (Chat)

```bash
ollama run mistral
```

You will see:

```
>>>
```

Type your prompt:

```text
Explain LangChain in one line
```

Exit:

```text
Ctrl + D
```

---

## Managing Models

### List models

```bash
ollama list
```

### Remove a model

```bash
ollama rm mistral
```

---

## Using Ollama with Python (Basic)

### Install Python client

```bash
pip install ollama
```

### Example

```python
import ollama

response = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Say hello'}]
)

print(response['message']['content'])
```

---

## Using Ollama with LangChain

### Install

```bash
pip install langchain langchain-community
```

### Example

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="mistral")
print(llm.invoke("Explain Ollama in one sentence").content)
```

---

## Auto-start Ollama (Optional)

### Start at boot

```bash
brew services start ollama
```

### Stop service

```bash
brew services stop ollama
```

---

## Common Issues & Fixes

### ❌ `could not connect to running Ollama instance`

**Fix:** Start server

```bash
ollama serve
```

### ❌ Port already in use

```bash
pkill ollama
ollama serve
```

### ❌ Slow responses

* Use smaller model (`phi`, `mistral`)
* Close heavy apps

---

## Disk Usage

| Component     | Size    |
| ------------- | ------- |
| Ollama binary | ~200 MB |
| One model     | 1–5 GB  |
| Typical setup | ~5–6 GB |

---

## When to Use Ollama

* Learning LangChain / LLMs
* Offline development
* Prototyping AI features
* Avoiding API costs

---

## When NOT to Use Ollama

* Production at large scale
* Real-time high concurrency
* GPU-heavy workloads (unless tuned)

---

## Summary (TL;DR)

* Ollama = **local AI runtime**
* Free, offline, developer-friendly
* Works perfectly with LangChain
* Ideal for learning & prototyping

---

✅ You now have a complete Ollama setup.

If you want, next steps can be:

* LangChain + SQL
* LangChain + PDFs (RAG)
* Performance tuning for M-series Macs
