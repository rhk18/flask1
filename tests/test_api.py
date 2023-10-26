import requests

def test_api_1():
    url="http://127.0.0.1:8000/v1/sanitized/input/"
    payload={"name":"rupesh"}
    response=requests.post(url,json=payload)
    expected_result={"result":"sanitised"}
    assert response.json()==expected_result

def test_api_2():
    url="http://127.0.0.1:8000/v1/sanitized/input/"
    payload={"name":"rupesh/"}
    response=requests.post(url,json=payload)
    expected_result={"result":"unsanitised"}
    assert response.json()==expected_result
