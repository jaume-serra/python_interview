from sqlalchemy.orm import Session
from db.models import Joke
from db.schemas import JokeSchema

def check_id(db: Session, updateId : int):
    return db.query(Joke).filter(Joke.id == updateId).first()

def check_existing(db: Session, joke: JokeSchema):
    exists = db.query(Joke).filter(Joke.value == joke.text).first() 
    if(exists):
        return True
    return False


def create_joke(db: Session, joke: JokeSchema):
    db.add(Joke(value=joke.text))
    db.commit()
    return db.query(Joke.id).filter(Joke.value == joke.text).first()
    
def put_joke(db: Session, joke : JokeSchema):
    db.query(Joke).filter(Joke.id == joke.number).update({Joke.value: joke.text})
    db.commit()
    
    
def delete_joke(db: Session, deleteId : int):
    db.query(Joke).filter(Joke.id == deleteId).delete()
    db.commit()
    
def deleteDb(db: Session):
    db.query(Joke).delete()
    db.commit()