from starlette.testclient import TestClient

from sql_app.main import app

client = TestClient(app)


def test_locations_postgres():
    response = client.get("/detect/77.05505847930908&28.524246963021376")
    assert response.status_code == 200
    assert response.json() == {
        "city": "Gurgaon",
        "area": "City",
        "state": "Haryana"
    }


def test_locations_postgres_existing():
    response = client.get("/detect/77&28")
    assert response.status_code == 404
    assert response.json() == {"detail": "The location you inserted is out of the our database."}