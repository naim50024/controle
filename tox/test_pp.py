from fastapi.testclient import TestClient
from main import app  # Assurez-vous que le nom du fichier est correct

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "Application fonctionne correctement"}
