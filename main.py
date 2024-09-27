from fastapi import FastAPI, Header, HTTPException
import os

app = FastAPI()

# Récupérer le jeton API depuis la variable d'environnement
API_TOKEN = os.getenv("GROQ_API_TOKEN")

@app.get("/status")
async def status(api_key: str = Header(...)):
    if api_key != API_TOKEN:
        raise HTTPException(status_code=403, detail="Jeton API invalide")
    return {"status": "Connexion réussie avec le jeton API Groq"}
