from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/api/pokemon/{name}")
async def get_pokemon(name: str):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Pokémon not found")
