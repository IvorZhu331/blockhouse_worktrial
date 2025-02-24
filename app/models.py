from pydantic import BaseModel

class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderResponse(Order):
    id: int

class ErrorResponse(BaseModel):
    detail: str
