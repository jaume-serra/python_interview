import requests

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.schemas import JokeSchema
from db.database import get_db
import db.crud as crud

jokesapp = APIRouter()

@jokesapp.get("/")
async def get_joke():
 
    joke =  requests.get("https://api.chucknorris.io/jokes/random").json()
    return {"detail": joke['value']}

@jokesapp.get("/{value}")
async def get_joke(value):
  
    if(value) == "Chuck":
        chuckJoke =  requests.get("https://api.chucknorris.io/jokes/random").json()
        return {"detail": chuckJoke['value']}
    
    if(value) == "dad":
        dadJoke = requests.get("https://icanhazdadjoke.com", headers = {'Accept': 'application/json'}).json()
        return {"detail": dadJoke['joke']}

    raise HTTPException(status_code=400, detail="Invalid Parameter")


@jokesapp.post("/")
async def post_joke(joke : JokeSchema, db: Session = Depends(get_db)):
    
    if(not joke.text):
        raise HTTPException(status_code=400, detail="Invalid Parameter. Joke can't be empty")
           
    if(crud.check_existing(db,joke)):
        raise HTTPException(status_code=400, detail="Invalid Parameter. Joke repeated")
        
    id = crud.create_joke(db, joke) 
    return {'detail': 'Joke created', 'id': id }
        
        
    
    


@jokesapp.put("/")
async def update_joke(joke: JokeSchema, db: Session = Depends(get_db)):

    if(not joke.text or not joke.number):
        raise HTTPException(status_code=400, detail="Invalid text or number")
    if not crud.check_id(db,joke.number):
        raise HTTPException(status_code=400, detail="Invalid number")

    crud.put_joke(db, joke)
    return {'detail': "Joke updated"}

    
@jokesapp.delete("/all")
async def delete_db_test(db: Session = Depends(get_db)):
    crud.deleteDb(db)
    return {'detail': 'Test db deleted'}
    
@jokesapp.delete("/{deleteId}")
async def delete_joke(deleteId, db: Session = Depends(get_db)):
    if not deleteId:
        raise HTTPException(status_code=400, detail="Invalid number")
    
    if (not crud.check_id(db,deleteId)):
        raise HTTPException(status_code=400, detail="Invalid number")
    crud.delete_joke(db, deleteId)
    
    return {'detail': "Joke deleted"}
    
    
    
    