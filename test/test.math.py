from urllib import response
from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def get_math_mcm():
    response = client.get("/math?numbers=[4,5,6]")
    assert response.status_code == 200
    assert response.json() == {'detail': 60}
    
def get_math_mcm_one():
    response = client.get("/math?numbers=[4]")
    assert response.status_code == 200
    assert response.json() == {'detail': 4}
    
def get_math_mcm_bad():
    response = client.get("/math?numbers=[]")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid parameter. Empty list'}
    
    
def get_plus():
    response = client.get("/math?numbers=1")
    assert response.status_code == 200
    assert response.json() == {'detail': 2}
    
def get_math_mcm_one():
    response = client.get("/math?numbers=s")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid parameter.'}
    
