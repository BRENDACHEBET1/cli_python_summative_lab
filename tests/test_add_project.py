def test_add_project():
    project = {
        "id": 1,
        "title": "Website",
        "description": "Build company site",
        "due_date": "2026-12-01",
        "user_email": "brenda@email.com"
    }

    assert project["title"] == "Website"
    assert project["user_email"] == "brenda@email.com"