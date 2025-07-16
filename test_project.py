import os
import json
import project

def test_add_stock():
    test_file = "test_portfolio.json"
    project.file_path = test_file  

    if os.path.exists(test_file):
        os.remove(test_file)

    project.add_stock("AAPL", 5, 150.0)

    with open(test_file, "r") as f:
        data = json.load(f)

    assert "AAPL" in data
    assert data["AAPL"]["quantity"] == 5
    assert data["AAPL"]["buy_price"] == 150.0

    os.remove(test_file)


def test_get_live_price():
    price = project.get_live_price("AAPL")
    assert isinstance(price, float) or price is None

def test_get_live_price_invalid():
    price = project.get_live_price("XYZNOTREAL")
    assert price is None
