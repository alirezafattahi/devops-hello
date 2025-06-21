import requests
import time

def wait_for_web():
    for _ in range(10):
        try:
            r = requests.get("http://localhost:5000/health")
            if r.status_code == 200:
                return
        except:
            time.sleep(1)
    raise Exception("Web service not responding")

def test_health():
    res = requests.get("http://localhost:5000/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
