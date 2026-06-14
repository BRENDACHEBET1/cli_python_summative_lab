from utils import save_data, load_data

def test_save_and_load():
    data = [
        {
            "id": 1,
            "name": "Brenda"
        }
    ]

    save_data("test.json", data)

    loaded = load_data("test.json")

    assert loaded == data