# AI Legal Document Analyzer

## Overview
The AI Legal Document Analyzer is a Streamlit-based application designed to assist legal professionals by leveraging advanced AI for intelligent document analysis and summarization. This tool allows users to upload PDF or TXT legal documents and receive AI-powered insights, including summarization of key clauses, identification of potential anomalies in contracts, and concise summaries of case law, facts, reasoning, and outcomes.


## Getting Started

### Prerequisites
Before running the application, ensure you have the following installed:
*   Python 3.8+
*   `uv` (fast Python package installer and resolver)

### Installation
1.  **Clone the repository (or save the code):**
    ```bash
    # If using Git
    git clone git@github.com:Fidelek84/agentic_ai.git
    cd ai-legal-document-analyzer
    # If just saving the code, navigate to the directory where you saved the Python file
    ```

2.  **Create a virtual environment and install dependencies using `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate # On Windows: `.venv\Scripts\activate`
    uv pip install streamlit PyPDF2 openai python-dotenv
    ```
    *Alternatively, if you have a `requirements.txt` file:*
    ```bash
    # Create requirements.txt (if you don't have one) with:
    # streamlit
    # PyPDF2
    # openai
    # python-dotenv
    # Then:
    uv venv
    source .venv/bin/activate # On Windows: `.venv\Scripts\activate`
    uv pip install -r requirements.txt
    ```

3.  **Set up your OpenAI API Key:**
    Create a `.env` file in the root directory of your project (the same location as `your_script_name.py`) and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_actual_openai_api_key_here"
    ```
    Replace `"your_actual_openai_api_key_here"` with your real OpenAI API key.

### Running the Application
1.  **Activate your virtual environment (if not already active):**
    ```bash
    source .venv/bin/activate # On Windows: `.venv\Scripts\activate`
    ```

2.  **Run the Streamlit app:**
    ```bash
    streamlit run your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `legal_analyzer.py`)

3.  The application will open in your web browser, typically at `http://localhost:8501`.

## Usage
1.  **Upload Document:** Click the "Browse files" button to upload your PDF or TXT legal document.
2.  **Select Analysis Focus:** Choose one or more options from the "Select analysis focus" dropdown to guide the AI's analysis.
3.  **Enter Custom Query (Optional):** If you have a specific question or instruction, type it into the "Enter a specific question or instruction for the AI" text box.
4.  **Analyze:** Click the "Analyze Document" button. The AI's analysis will appear below.