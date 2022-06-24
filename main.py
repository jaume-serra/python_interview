from fastapi import FastAPI

from src.jokes import jokesapp
app = FastAPI()
app.include_router(jokesapp, prefix="/jokes")

@app.get("/")
async def read_main():
    return {"detail": "Hi There, you can visit /jokes or /math"}