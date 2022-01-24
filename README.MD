Fizz Buzz

`To run the application as a docker container`

1. Create an image using the command below ()

docker build --tag <image-name> .

2. Run the docker image with the following command to map host port with container port 8000

docker run --publish 8000:8000 <image-name>

`To run the application on your local`

Dependencies required to run this app

1. fastapi
2. uvicorn
3. requests
4. pytest

After installing all the dependencies run the app by running the command inside the folder
containing the python files

`uvicorn main:app --reload`

API endpoints

1. /fizzbuzz/entities - a GET API endpoint that sends an array of 10 fizz buzz entities

2. /fizzbuzz/{number} - a GET API endpoint that determines the type of fizz buzz entitty for a given number and also shows the placeholder title and body in the response from https://jsonplaceholder.typicode.com/guide/
