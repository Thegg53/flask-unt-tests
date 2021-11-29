def test_double(client, x=45):
    response = client.get(f"/double/{x}")
    assert response.data == b"<div>your result is:</div>90"