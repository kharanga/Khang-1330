from typing import List
import spacy
from fastapi import FastAPI

app = FastAPI()
nlp = spacy.load("en_core_web_md")

@app.post("/ner")
def process_text(sentence: str):
    document = nlp(sentence)
    result = []
    for entity in document.ents:
        temp = {}
        temp["entity"] = entity.label_
        temp["value"] = entity.text
        result.append(temp)
    return {"result": result}
