# **SciBite ML Python Homework**
# Preface
Out of the four additional tasks in the list provided, I completed numbers #2, #3 & #4. I only chose to do #2 purely for fun/a challenge as I have a small amount of experience with frontend dev work through personal projects (though very rusty!), so just wanted to try and demonstrate talking to the API built in #3 with the most basic frontend possible... so please don't be too hard on my possibly less-than-idiomatic JavaScript code!

As, in the end, there were distinct 'services' within the codebase, I decided to use docker and docker-compose to make the running of the codebase much simpler... plus, who doesn't love docker?!

For the API implementation, instead of using Flask, I decided to use a framework that I have also become very fond of: [FastAPI](https://fastapi.tiangolo.com/). It's just as easy as Flask to use, but comes with some extra bells and whistles. It is built on ASGI server implementations such as [uvicorn](https://www.uvicorn.org/), which means that it is super-fast - even in competition with more traditionally performant languages such as Golang and Node(JS).

# Prerequisites / Dependencies
All that is needed for running the project is [docker](https://docs.docker.com/engine/install/) & [docker-compose](https://docs.docker.com/compose/install/). *(See installation guides if needed)* 

For Python dependencies I like to use [pipenv](https://github.com/pypa/pipenv), which is the Python recommended package manager, for which the packages are defined in the [Pipfile](https://github.com/AdamJRPond/text-cleaner/blob/main/Pipfile). 

JavaScript dependencies are defined in the [package.json](https://github.com/AdamJRPond/text-cleaner/blob/main/frontend/[package.json]) and I used [yarn](https://yarnpkg.com/) as the package manager.

Both Python and JavaScript dependencies will be downloaded and installed at build-time of the docker services.

## Clone Project
```bash
git clone https://github.com/AdamJRPond/text-cleaner.git
```
# How to run

## Build docker container
#### From the root of the repository, execute:
```bash
docker-compose up --build
```
On the first time this will take a few minutes to pull the image and setup the dependencies for each container.

## Tests
To run the tests inside of the docker container, first access the containers terminal...

*NOTE: You may need to use* `sudo` *depending on your local docker config*
```bash
docker exec -it fastapi "/bin/bash"
```

Then, inside the container's terminal...
```bash
pipenv run python -m unittest
```
## Main task
The code that executes the main functionality of transforming a string of text/abstract is inside of the `clean_text` function inside of [utils.py](https://github.com/AdamJRPond/text-cleaner/blob/main/utils.py).

This functionality is demonstrating within the additional tasks, but the primary task of transforming the batch of abstracts provided in [abstract_test_data_file.txt](https://github.com/AdamJRPond/text-cleaner/blob/main/tests/test_data/abstract_test_data_file.txt) is demonstrated within the [test_utils.py](https://github.com/AdamJRPond/text-cleaner/blob/main/tests/test_utils.py) testcase.

On running the unit tests, the results of the batch transformation are saved to [test_output.csv](https://github.com/AdamJRPond/text-cleaner/blob/main/tests/test_data/test_output.csv) (a version is already inside the repo) for demonstration purposes. A docker volume has been mapped to the local 'test' folder, so the output will be available locally as well as inside the container.

## #2 | Frontend
The frontend is accessible at [http://localhost:8080/](http://localhost:8080/).

Just enter any body of text in the text box provided, then click the button to submit and the text will be transformed using the API built in #3.

## #3 | API
The API endpoint is exposed at [http://localhost:8000/clean/](http://localhost:8000/clean/).

Also, if you go to [http://localhost:8000/docs](http://localhost:8000/docs), you will find automatically generated Swagger/OpenAPI documentation which shows all the methods relating to that endpoint (in this case we only have one). You can also use this to test the APIs with your own data, which is not only good for development, but useful for demonstrating the API in this instance.

Alternatively, another easy way to hit the API is using cURL - something like this:

```bash
curl -X POST "http://localhost:8000/clean/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"pub_id\":\"string\",\"abstract\":\"<ENTER ANY TEXT HERE>"
```

There is also a simple unit test for the API with a local test client inside of [test_main.py](https://github.com/AdamJRPond/text-cleaner/blob/main/tests/test_main.py)

## #4 | TF-IDF 
Similarly to the main task, this task is demonstrated within the context of a testcase inside of [test_utils.py](https://github.com/AdamJRPond/text-cleaner/blob/main/tests/test_utils.py), and operates on all of the test data provided.
___
