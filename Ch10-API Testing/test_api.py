import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_api():
    #arrange
    url = "https://api.duckduckgo.com/?q=Python+programming&format=json" #it takes two parameters first:?q=python+programming second:format=json

    #act
    response = requests.get(url) #send the http send request
    body = response.json()

    #assert
    assert response.status_code == 200 #to verify the request was successfull
    assert 'Python' in body['AbstractText'] #it will check the response of the content, if the search for python programming is successful it would chekc the python word
