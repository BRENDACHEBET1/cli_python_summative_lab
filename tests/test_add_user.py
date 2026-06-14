def test_add_user():
    user = {
        "id": 1,
        "name": "Brenda",
        "email": "brenda@email.com"
    }

    assert user["name"] == "Brenda"
    assert user["email"] == "brenda@email.com"