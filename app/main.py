from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request model
class TextInput(BaseModel):
    text: str

@app.post("/process/")
async def process_input(data: TextInput):
    logger.info(f"Received input: {data.text}")
    return {"response": f"Processed: {data.text}"}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the AI Voice Assistant API!"}
