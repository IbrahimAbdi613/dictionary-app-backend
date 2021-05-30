from fastapi import FastAPI
import os
import requests

app = FastAPI()

@app.get("/")
def home():
    return{"Hello":"World"}

@app.get("/{word}")
def getWord(word):
    response = requests.get(
        "https://wordsapiv1.p.rapidapi.com/words/" + word, 
        headers={"X-Mashape-Key": os.getenv('WORDS_API_KEY')}
    )
    return {"Data":response.json()}

    