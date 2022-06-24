from urllib import response
from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_joke():
    response = client.get("/jokes/")
    assert response.status_code == 200

def test_get_joke_chuck():
    response = client.get("/jokes/Chuck")
    assert response.status_code == 200
    assert "Chuck" in response.json().value()

def test_get_joke_dad():
    response = client.get("/jokes/Dad")
    assert response.status_code == 200
    assert "Dad" in response.json().value()


def test_get_joke_bad():
    response = client.get("/jokes/Bob")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid Parameter'}


def test_post_joke():
    response = client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    assert response.status_code == 200
    assert response.json() == {'detail': 'Joke created'}


def test_post_joke_bad():
    response = client.post("/jokes/", json={'text': ''})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid Parameter. Joke can't be empty"}
    
    
def test_update_joke():
    response = client.update("/jokes/", json={'number': 0, 'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    assert response.status_code == 200
    assert response.json() == {'detail': "Joke updated"}

    
def test_update_joke_bad():
    response = client.update("/jokes/", json={'number': 9999, 'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid Number"}


def test_delete_joke():
    response = client.delete("/jokes/", json={'number': 0})
    assert response.status_code == 200
    assert response.json() == {'detail': "Joke deleted"}
        
def test_delete_joke_bad():
    response = client.delete("/jokes/", json={'number': 999})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid number"}
        


    
    
