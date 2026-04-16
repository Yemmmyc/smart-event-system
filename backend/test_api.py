from main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_crowd():
    client = app.test_client()
    response = client.get("/crowd")
    assert response.status_code == 200

def test_alerts():
    client = app.test_client()
    response = client.get("/alerts")
    assert response.status_code == 200