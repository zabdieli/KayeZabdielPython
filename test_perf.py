import time

def test_response_time(client):
    start = time.time()
    client.get('/')
    end = time.time()
    assert (end - start) < 0.5 
