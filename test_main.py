from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# Test case to validate status code of get endpoint /fizzbuzz/entities


def test_get_entities():
    response = client.get("/fizzbuzz/entities")
    assert response.status_code == 200


# Test case to validate the 10 fizz buzz response of get endpoint /fizzbuzz/entities


def test_response_get_entities():
    response = client.get("/fizzbuzz/entities")
    assert response.json() == [3, 5, 6, 9, 10, 12, 15, 18, 20, 21]


# Test case to validate the status code  of get endpoint /fizzbuzz/{number}


def test_sc_fizzbuzz():
    response = client.get("/fizzbuzz/3")
    assert response.status_code == 200


# Test case to validate the fizzbuzz response of get endpoint /fizzbuzz/{number} is "fizz"


def test_fizz_fizzbuzz():
    response = client.get("/fizzbuzz/3")
    assert response.json()['fizzbuzz'] == "fizz"


# Test case to validate the fizzbuzz  response of get endpoint /fizzbuzz/{number} is "buzz"

def test_buzz_fizzbuzz():
    response = client.get("/fizzbuzz/5")
    assert response.json()['fizzbuzz'] == "buzz"

# Test case to validate the fizzbuzz response of get endpoint /fizzbuzz/{number} is "fizzbuzz"


def test_fizzbuzz_fizzbuzz():
    response = client.get("/fizzbuzz/15")
    assert response.json()['fizzbuzz'] == "fizzbuzz"


# Test case to validate the fizzbuzz response of get endpoint /fizzbuzz/{number} is "null / none"


def test_none_fizzbuzz():
    response = client.get("/fizzbuzz/2")
    assert response.json()['fizzbuzz'] == None

# Test case to validate the placeholder_post response of get endpoint /fizzbuzz/{number} is not empty


def test_is_not_none_placeholder_fizzbuzz():
    response = client.get("/fizzbuzz/1")
    assert response.json()['placeholder_post']['title'] != None
    assert response.json()['placeholder_post']['body'] != None


# Test case to validate the placeholder_post response of get endpoint /fizzbuzz/{number} is empty


def test_none_placeholder_fizzbuzz():
    response = client.get("/fizzbuzz/1000")
    assert response.json()['placeholder_post']['title'] == ""
    assert response.json()['placeholder_post']['body'] == ""
