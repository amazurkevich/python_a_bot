from fastapi import FastAPI
import json
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chuck")
def chuck():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    contents = json.loads(response.content)

    return contents["value"]