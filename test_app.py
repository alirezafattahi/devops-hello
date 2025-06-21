import requests

def test_health():
    res = requests.get("http://web:5000/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
