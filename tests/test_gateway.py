import pytest
from fastapi.testclient import TestClient

from gateway import app

client = TestClient(app)


def test_open_car():
    response = client.get("/open")

    assert "car opened" in response.text


def test_close_car():
    response = client.get("/close")

    assert "car closed" in response.text


def test_open_windows():
    response = client.get("/open_windows")

    assert response.status_code == 200


def test_get_fuel():
    response = client.get("/get_fuel")

    assert response.status_code == 200



def test_get_accumulator_charge():
    response = client.get("/get_accumulator_charge")

    assert response.status_code == 200



def test_get_oil_temp():
    response = client.get("/get_oil_temp")

    assert response.status_code == 200


def test_get_engine_temp():
    response = client.get("/get_engine_temp")

    assert response.status_code == 200



def test_set_temperature_start_engine():
    response = client.post(
        "/set_temperature_start_engine",
        params={"temperature": -10}
    )

    assert response.status_code == 200


def test_start_engine():
    response = client.get("/start_engine")

    assert response.status_code == 200