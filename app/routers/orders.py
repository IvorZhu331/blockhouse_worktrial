from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Order, OrderResponse, ErrorResponse
from app.database import get_db_connection

router = APIRouter(prefix="/orders", tags=["orders"])

# POST /orders
@router.post("/", response_model=OrderResponse, responses={400: {"model": ErrorResponse}})
def create_order(order: Order):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO orders (symbol, price, quantity, order_type) VALUES (?, ?, ?, ?)",
                       (order.symbol, order.price, order.quantity, order.order_type))
        conn.commit()
        order_id = cursor.lastrowid
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=400, detail=str(e))

    conn.close()
    return OrderResponse(id=order_id, **order.model_dump())

# GET /orders
@router.get("/", response_model=List[OrderResponse])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, symbol, price, quantity, order_type FROM orders")
    rows = cursor.fetchall()

    conn.close()

    return [OrderResponse(id=row["id"], symbol=row["symbol"], price=row["price"],
                          quantity=row["quantity"], order_type=row["order_type"]) for row in rows]

# DELETE /orders/{order_id}
@router.delete("/{order_id}", response_model=OrderResponse, responses={404: {"model": ErrorResponse}})
def delete_order(order_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    order = cursor.fetchone()

    if not order:
        conn.close()
        raise HTTPException(status_code=404, detail="Order not found")

    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()

    return OrderResponse(id=order["id"], symbol=order["symbol"], price=order["price"],
                         quantity=order["quantity"], order_type=order["order_type"])
