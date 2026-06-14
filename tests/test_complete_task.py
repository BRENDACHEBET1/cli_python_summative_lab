def test_complete_task():
    task = {
        "id": 1,
        "title": "Design homepage",
        "status": "pending"
    }

    task["status"] = "completed"

    assert task["status"] == "completed"