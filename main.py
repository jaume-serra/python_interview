from fastapi import FastAPI
from src.jokes import jokesapp
from src.math import mathapp

app = FastAPI()

app.include_router(jokesapp, prefix="/jokes")
app.include_router(mathapp, prefix="/math")



@app.get("/")
async def read_main():
    return {"detail": "Hi There, you can visit /jokes or /math"}

