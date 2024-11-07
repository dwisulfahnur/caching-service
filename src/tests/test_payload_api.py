import pytest
from fastapi.testclient import TestClient

def test_create_payload(client: TestClient):
    response = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    identifier = data["id"]

    assert response.headers["X-Cached"] == "0"
    assert identifier


def test_cached_payload(client: TestClient):
    payload = {
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    }
    response = client.post("/payload", json=payload)
    data = response.json()
    identifier = data["id"]

    assert response.status_code == 201

    # post new payload with the same payload as the first
    cached_response = client.post("/payload", json=payload)
    cached_data = cached_response.json()

    assert cached_response.status_code == 200
    assert cached_data["id"] == identifier
    assert cached_response.headers["X-Cached"] == "1"


def test_different_payloads(client: TestClient):
    response_1 = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })

    response_2 = client.post("/payload", json={
        "list_1": ["new string", "another new string", "final string"],
        "list_2": ["another entry", "second entry", "third entry"]
    })

    data_1 = response_1.json()
    data_2 = response_2.json()

    assert data_1["id"] != data_2["id"]

    assert response_1.status_code == 201
    assert response_1.headers["X-Cached"] == "0"


    assert response_2.status_code == 201
    assert response_2.headers["X-Cached"] == "0"


def test_retrieve_payload(client: TestClient):
    create_response = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })
    identifier = create_response.json()["id"]

    get_response = client.get(f"/payload/{identifier}")
    assert get_response.status_code == 200
    assert "output" in get_response.json()



def test_retrieve_payload_not_found(client: TestClient):
    identifier = "unknownidentifier"

    get_response = client.get(f"/payload/{identifier}")
    assert get_response.status_code == 404
