from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_no_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "")
    response = client.post("/chat", json={"message": "What is CI/CD?"})
    assert response.status_code == 500
    assert "OpenAI API key not configured" in response.text
