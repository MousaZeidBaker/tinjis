from fastapi.testclient import TestClient

from payment.main import app

client = TestClient(app)


def test_read_health():
    response = client.get("/v1/healthz")
    assert response.status_code == 200
    assert response.json() == {
        "status": "pass",
        "description": "NOT IMPLEMENTED",
    }


def test_create_payment():
    response = client.post(
        "/v1/payments",
        headers={"accept": "application/json"},
        json={
            "currency": "DKK",
            "value": 100,
            "customer_id": "1234",
        },
    )

    assert response.status_code == 200
