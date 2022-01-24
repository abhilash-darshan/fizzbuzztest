from fastapi import FastAPI
import requests

app = FastAPI()

# function to retrieve an array of 10 fizzbuzz entities


def get_fizz_buzz_entities():
    count = 0
    fizzbuzz = 1
    fizzbuzz_entities = []

    while count < 10:
        entity_value = return_fizz_buzz_value(fizzbuzz)

        if entity_value == None:
            fizzbuzz += 1
            continue
        else:
            count += 1
            fizzbuzz_entities.append(fizzbuzz)
            fizzbuzz += 1

    return fizzbuzz_entities

# function to determine if a number is of type "fizz" or "buzz" or "fizzbuzz" or "none"


def return_fizz_buzz_value(fizzbuzz):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        return "fizzbuzz"
    elif fizzbuzz % 3 == 0:
        return "fizz"
    elif fizzbuzz % 5 == 0:
        return "buzz"

    return None

# GET endpoint to retrieve first 10 fizzbuzz entities


@app.get("/fizzbuzz/entities")
def get_entities():
    fbe = get_fizz_buzz_entities()
    return fbe


''' GET endpoint that accepts a number as path parameter 
    and its response payload, mentions whether the number is a fizz buzz entity
    and provides the title & body from the https://jsonplaceholder.typicode.com/guide/ 
    in the placeholder_post object
'''


@app.get("/fizzbuzz/{item_id}")
def read_item(item_id: int):

    api_response = {
        "number": 1,
        "fizzbuzz": None,
        "placeholder_post": {
            "title": "",
            "body": ""
        }
    }

    api_response["number"] = item_id
    api_response["fizzbuzz"] = return_fizz_buzz_value(item_id)
    URL = "https://jsonplaceholder.typicode.com/posts/" + str(item_id)
    result = requests.get(URL)

    if "title" in result.json():
        api_response["placeholder_post"]["title"] = result.json()['title']

    if "body" in result.json():
        api_response["placeholder_post"]["body"] = result.json()['body']

    return api_response
