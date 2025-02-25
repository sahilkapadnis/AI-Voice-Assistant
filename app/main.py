from fastapi import FastAPI
from pydantic import BaseModel
import logging
from app.nlp import process_text

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextInput(BaseModel):
    text: str

@app.post("/process/")
async def process_input(data: TextInput):
    logger.info(f"Received input: {data.text}")
    response = process_text(data.text)
    return {"response": response}
