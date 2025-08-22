# Project1

```
p1/
├── src/
│   └── main.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Description

Project1 is a Python-based application that utilizes LangChain framework and OpenAI capabilities.

## Requirements

- Python >= 3.13
- Dependencies:
  - langchain >= 0.3.27
  - langchain-openai >= 0.3.30
  - langgraph >= 0.6.5
  - python-dotenv >= 1.1.1

## Installation

1. Clone the repository
2. Create a virtual environment:
```sh
python -m venv env
source env/bin/activate  # On Unix/macOS
# or
.\env\Scripts\activate  # On Windows
```
3. Install dependencies:
```sh
pip install -e .
```

## Environment Setup

Create a `.env` file in the root directory and add your environment variables:
```sh
OPENAI_API_KEY=your_api_key_here
```