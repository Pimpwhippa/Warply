
task python developer

Your task is to create a microservice with a tornado API endpoint that you will design using the bitmap roaring implementation in python that you can find here (https://github.com/Ezibenroc/PyRoaringBitMap).


We need tests that will test the following use cases:

    session management: how many users have not log in for a week?
    user tagging with tags (tag1....tag10) and answer to the question: how many users have tag1 and tag2, what are the ids of users with tag1
    load test for 1000 concurrent sessions

activate virtual environment:
pipenv shell

install package: 
pipenv install -e .

launch app in cli:
serve_app
