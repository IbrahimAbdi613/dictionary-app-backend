from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

import os
import requests
load_dotenv()

app = FastAPI()

origins = [
    "https://dictionary-ibrahim.netlify.app/",
    "https://dictionary-ibrahim.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    