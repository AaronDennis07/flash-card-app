from fastapi import FastAPI
from contextlib import asynccontextmanager
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from fastapi import File, UploadFile
import os
import helpers
import json

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.5)
chat_template= ChatPromptTemplate.from_messages(
        [
            ("system", """You are an expert flashcard generator given the user input output 10 flashcards 
            containing question answer and a short explanation return the response in 
            json such that the output can be directly parsed to python dictionary
            """),
            ("human","{content}")
        ]
    )


app = FastAPI()

@app.post("/api/v1/flashcards")
def get_flash_cards(file: UploadFile = File(...)):

    try:
        contents = file.file.read()
        with open('data/'+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    data = helpers.load_document('data/'+file.filename)
    content = helpers.extract_input(data)
    response = llm.invoke(chat_template.format(content=content))
    os.remove('data/'+file.filename)

    return json.loads(response.content)['flashcards']



