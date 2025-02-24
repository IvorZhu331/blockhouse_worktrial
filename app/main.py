from fastapi import FastAPI
from app.routers import orders

app = FastAPI(
    title="Trade Order API",
    description="A FastAPI backend for managing trade orders.",
    version="1.0.0"
)

# Include the orders router
app.include_router(orders.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Trade Order API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="54.163.82.225", port=8000, reload=True)
