def test_add_task():
    task = {
        "id": 1,
        "title": "Design homepage",
        "status": "pending",
        "project_id": 1,
        "assigned_to": "brenda@email.com"
    }

    assert task["status"] == "pending"