# SAP Transaction Code Explainer API

An AI-powered REST API that helps SAP consultants understand
transaction codes, explore modules, and troubleshoot common errors.

## Endpoints

- `GET /explain/{tcode}` — Plain English explanation of any SAP transaction code
- `GET /tcodes/{module}` — List transaction codes by SAP module (FI, MM, SD, BASIS)
- `GET /troubleshoot/{tcode}` — Common errors and fixes for a transaction code

## Tech Stack

- Python, FastAPI, OpenAI GPT-4o-mini

## Setup

1. Clone the repo
2. Create a `.env` file with `OPENAI_API_KEY=your-key`
3. Run `pip install fastapi uvicorn openai python-dotenv`
4. Run `uvicorn main:app --reload`
5. Visit `https://sap-tcode-explainer.onrender.com/docs`


