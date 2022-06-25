from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

""" Joke Tests """

def test_get_joke():
    response = client.get("/jokes/")
    assert response.status_code == 200

def test_get_joke_chuck():
    response = client.get("/jokes/Chuck")
    assert response.status_code == 200
    assert "Chuck" in response.json()['detail']

def test_get_joke_dad():
    response = client.get("/jokes/dad")
    assert response.status_code == 200

def test_get_joke_bad():
    response = client.get("/jokes/Bob")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid Parameter'}



def test_post_joke():
    client.delete("/jokes/all", json={})
    response = client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    print(response.json()['detail'])
   
    assert response.status_code == 200
    assert response.json()['detail'] == 'Joke created'


def test_post_joke_bad():
    response = client.post("/jokes/", json={'text': ''})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid Parameter. Joke can't be empty"}


def test_post_joke_repeated():
    client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    response = client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid Parameter. Joke repeated"}
    
    
    
def test_update_joke():
    client.delete("/jokes/all", json={})
    res = client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    id = res.json()['id']['id']
    response = client.put("/jokes/", json={'number': id, 'text': 'Changed text'})
    assert response.status_code == 200
    assert response.json() == {'detail': "Joke updated"}


def test_update_joke_empty():
    response = client.put("/jokes/", json={'number': 1, 'text': ''})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid text or number"}



 
def test_update_joke_bad():
    response = client.put("/jokes/", json={'number': 9999, 'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid number"}



def test_delete_joke():
    client.delete("/jokes/all", json={})
    res = client.post("/jokes/", json={'text': 'Never look a gift Chuck Norris in the mouth, because he will bite your damn nose off.'})
    id = res.json()['id']['id']
    print(id)
    response = client.delete("/jokes/"+str(id))
    assert response.status_code == 200
    assert response.json() == {'detail': "Joke deleted"}
        
        
def test_delete_joke_bad():
    response = client.delete("/jokes/999")
    assert response.status_code == 400
    assert response.json() == {'detail': "Invalid number"}
    
        

