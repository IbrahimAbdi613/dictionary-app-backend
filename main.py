from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests
load_dotenv()

app = FastAPI()

@app.get("/") 
def home():
    return{"Hello":"World"}

@app.get("/{word}")
def getWord(word): 
    response = requests.get(
        "https://wordsapiv1.p.rapidapi.com/words/" + word, 
        headers={"X-Mashape-Key": os.environ.get('WORDS_API_KEY')}
    )
    print(os.environ.get('WORDS_API_KEY'))
    return {"Data":response.json()}

    