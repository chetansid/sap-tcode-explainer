from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/explain/{tcode}")
def explain_tcode(tcode: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Explain SAP transaction code {tcode} in plain English. Include: what it does, when to use it, and one common mistake beginners make."
            }]
        )
        return {"tcode": tcode, "explanation": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}