def test_hello_root(client):
    response = client.get("/")
    assert response.data == b"<p>Hello, World!</p>"