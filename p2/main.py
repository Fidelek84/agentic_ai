import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Legal Document Analyzer", page_icon="⚖️", layout="centered")
st.title("AI Legal Document Analyzer")
st.markdown("Upload a legal document (Contract, Case Law, etc.) for AI-powered analysis and summarization.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your legal document (PDF or TXT)", type=["pdf", "txt"])

analysis_focus = st.multiselect(
    "Select analysis focus (optional):",
    ["Contract Review: Summarize key clauses & identify potential issues/anomalies",
     "Case Law: Summarize facts, legal reasoning, and outcome",
     "Compliance Audit: Extract specific compliance-related information",
     "General Summary: Concisely summarize main points"],
    default="General Summary: Concisely summarize main points"
)
custom_query = st.text_input("Enter a specific question or instruction for the AI (optional):")

analyze = st.button("Analyze Document")

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text if text.strip() else None
    except PyPDF2.errors.PdfReadError:
        st.error("Error reading PDF. It might be encrypted or corrupted.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred during PDF text extraction: {e}")
        return None

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    try:
        return uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Could not decode text file. Ensure it's a plain text file (UTF-8 encoding preferred).")
        return None

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content or not file_content.strip():
            st.error("File does not have any content or text could not be extracted.")
            st.stop()
        
        prompt_instructions = ""
        if "Contract Review: Summarize key clauses & identify potential issues/anomalies" in analysis_focus:
            prompt_instructions += "Analyze this contract. Summarize its key clauses, obligations, and terms. Identify any potential anomalies, ambiguous language, missing standard clauses, or noteworthy risks. Highlight these points clearly.\n"
        if "Case Law: Summarize facts, legal reasoning, and outcome" in analysis_focus:
            prompt_instructions += "Analyze this case law document. Provide a concise summary of the factual background, the legal questions addressed, the court's reasoning, and the final outcome or holding.\n"
        if "Compliance Audit: Extract specific compliance-related information" in analysis_focus:
             prompt_instructions += "Analyze this regulatory document. Extract and summarize all sections pertaining to compliance requirements, penalties for non-compliance, and reporting obligations. If a specific compliance query is provided, focus on that.\n"
        if "General Summary: Concisely summarize main points" in analysis_focus and not prompt_instructions: 
            prompt_instructions += "Provide a concise summary of the main points and key information contained within this document.\n"
        
        if custom_query:
            prompt_instructions += f"Additionally, specifically address this request: '{custom_query}'\n"
        
        if not prompt_instructions and analysis_focus:
            prompt_instructions = "Based on the selected options, provide a clear and structured analysis.\n"
        elif not prompt_instructions and not analysis_focus:
             prompt_instructions = "Provide a concise summary and analysis of the document.\n"

        prompt = f"""You are an expert legal assistant with extensive knowledge in contract law, case law analysis, and regulatory compliance.
        Your task is to analyze the following legal document based on the provided instructions.
        
        Instructions:\n{prompt_instructions}
        
        Document content:
        {file_content}
        
        Please provide your analysis in a clear, structured, and legally precise format. If identifying anomalies or risks, state why they are noteworthy."""
        
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a highly skilled AI legal assistant. Provide legally accurate and concise summaries/analyses."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        st.markdown("### Legal Document Analysis Results")
        st.markdown(response.choices[0].message.content)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
