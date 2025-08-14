from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_redirect():
    res = client.post("/api/shorten", json={"url": "http://example.com"})
    assert res.status_code == 200
    code = res.json()["code"]

    res2 = client.get(f"/{code}", allow_redirects=False)
    assert res2.status_code == 307 or res2.status_code == 302
