from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/health")
async def get_health_status():
    return {"status":"up and running"}

client = TestClient(app)

@app.get("/")
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

@app.get("/health")
def get_health_status():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"up and running"}