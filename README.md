# Production RAG

This is a production implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

## Setup

### 1. Install uv

Download and install uv from [here](https://docs.astral.sh/uv/getting-started/installation/)

### 2. Setup environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `GEMINI_API_KEY` value.

## Run the FastAPI server

```bash
$ uv run dev
```

`uv` will automatically create a virtual environment and install all dependencies when you run this command.
