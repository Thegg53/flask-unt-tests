def test_triple(client, x=45):
    response = client.get(f"/triple/{x}")
    assert response.data == b"<div>triple is:</div>135"
