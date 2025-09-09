from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv


app = FastAPI()
load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/")
def root_controller():
    return {"status": "healthy"}


@app.get("/chat")
def chat_controller(prompt: str = "Inspire me"):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    statement = response.choices[0].message.content
    return {"statement": statement}
