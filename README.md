# AI-Powered Insurance Policy Document Extractor

A hands-on LLM + Pydantic project that extracts insurance policy details from PDF, DOCX, and TXT documents and validates the result as structured JSON.

## Features

- Groq cloud API or local Ollama through an OpenAI-compatible client
- PDF, DOCX, and TXT text extraction
- Page-aware chunking for longer documents
- Pydantic v2 nested schemas and field constraints
- JSON-mode LLM responses followed by Pydantic validation
- Evidence quotes and page references
- Explicit handling of missing and conflicting values
- CLI output saved as JSON

## 1. Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Use your existing `.env` in this project directory. Expected variables:

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_real_key
# Optional:
# LLM_MODEL=openai/gpt-oss-120b
# OLLAMA_BASE_URL=http://localhost:11434/v1
```

Do not commit `.env`. Add it to `.gitignore`.

For Ollama, pull a compatible model and start Ollama:

```bash
ollama pull qwen2.5:3b
ollama serve
```

Then set `LLM_PROVIDER=ollama` in `.env`. No Groq key is needed for Ollama.

## 2. Run

```bash
python main.py data/sample_policy.pdf
```

Choose a custom output:

```bash
python main.py data/sample_policy.pdf --output outputs/my_policy.json
```

Supported formats: `.pdf`, `.docx`, `.txt`.

## 3. Project structure

```text
insurance_policy_extractor/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── insurance_policy_extractor.ipynb
├── src/
│   ├── __init__.py
│   ├── schemas.py
│   ├── document_reader.py
│   ├── llm_client.py
│   └── extractor.py
├── data/
└── outputs/
```

## 4. Extraction schema

The Pydantic output includes insurer/product identity, policy number and UIN, policyholder and insured people, policy dates, premium, sum insured, benefits, exclusions, waiting periods, riders, claim steps, important conditions, missing/unclear items, and evidence.

Unknown facts must be `null` or an empty list. Evidence quotes should be checked against the original document before downstream decisions.

## 5. Important limitations

- Scanned PDFs need OCR; this starter project detects empty text extraction and stops rather than guessing.
- Chunk merging can still miss or misattribute facts. Review evidence and compare with the source policy.
- LLM output is not authoritative. Do not use this project alone to approve claims, determine coverage, or make legal/financial decisions.
- Page numbers are supplied for PDFs. DOCX and TXT inputs do not have reliable page numbers.
- Protect policy documents and API traffic; they may contain sensitive personal and financial information.

## 6. Suggested extensions

1. OCR for scanned PDFs using Tesseract or a managed document OCR service.
2. Add a review UI where users can click evidence and verify each field.
3. Add a second-model judge for evidence support and extraction completeness.
4. Add unit tests with synthetic policies and known expected JSON.
5. Add FastAPI upload and extraction endpoints, background jobs, and persistent audit logs.
6. Add document-level comparison between policy schedule, wording, and endorsements.
