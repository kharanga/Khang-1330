from typing import List
import spacy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

#An object that store the entity and value of a Span
class Text(BaseModel):
    entity: str
    value: str

#The return type from the server side to the clien side
class Result(BaseModel):
    result: List[Text]

#Pass in a sentence to be examine
@app.post("/ner", response_model=Result)
def process_text(sentence: str):
    document = nlp(sentence)
    result = []
    #Loop through every entity and store it respective value in the result array
    for entity in document.ents:
        temp = {}
        temp["entity"] = entity.label_
        temp["value"] = entity.text
        result.append(temp)
    return {"result": result}
