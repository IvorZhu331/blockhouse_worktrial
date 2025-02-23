from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

sample_order = {
    "symbol": "AAPL",
    "price": 150.25,
    "quantity": 10,
    "order_type": "buy"
}

def test_create_order():
    response = client.post("/orders/", json=sample_order)
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == sample_order["symbol"]
    assert data["price"] == sample_order["price"]
    assert data["quantity"] == sample_order["quantity"]
    assert data["order_type"] == sample_order["order_type"]
    assert "id" in data

def test_get_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_delete_order():
    create_response = client.post("/orders/", json=sample_order)
    order_id = create_response.json()["id"]

    delete_response = client.delete(f"/orders/{order_id}")
    assert delete_response.status_code == 200
    
    get_response = client.get("/orders/")
    orders = get_response.json()
    assert all(order["id"] != order_id for order in orders)

def test_delete_nonexistent_order():
    response = client.delete("/orders/99999")  # Assuming this ID doesn't exist
    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"
