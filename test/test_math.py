from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_math_mcm():
    response = client.get("/math/mcm/[4,5,6]")
    assert response.status_code == 200
    assert response.json() == {'result': 60}
    
def test_get_math_mcm_one():
    response = client.get("/math/mcm/[4]")
    assert response.status_code == 200
    assert response.json() == {'result': 4}
    
def test_get_math_mcm_bad():
    response = client.get("/math/mcm/[]")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid parameter. Empty list'}
    
def test_get_math_mcm_invalid():
    response = client.get("/math/mcm/[1,2,'s']")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid parameter.'}
    

    
def test_get_plus():
    response = client.get("/math/plus/1")
    assert response.status_code == 200
    assert response.json() == {'result': 2}


def test_get_math_plus_bad():
    response = client.get("/math/plus/s")
    assert response.status_code == 422
    
