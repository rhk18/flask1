import requests

def test_api():
    url="http://127.0.0.1:8000/v1/sanitized/input/"

    payload1={"name":"rupesh"}
    payload2={"name":"rupesh--"}

    response1=requests.post(url,json=payload1)
    response2=requests.post(url,json=payload2)

    
    expected_result1={"result":"sanitised"}
    expected_result2={"result":"unsanitised"}

    assert response1.json()==expected_result1
    assert response2.json()==expected_result2

