from fastapi import FastAPI
import os
import requests

app = FastAPI()


@app.get("/{word}")
def home(word):
    response = requests.get(
        "https://wordsapiv1.p.rapidapi.com/words/" + word, 
        headers={"X-Mashape-Key": os.getenv('WORDS_API_KEY')}
    )
    return {"Data":response.json()}

    