# This is a sample Python script using FastAPI
from fastapi import FastAPI
app = FastAPI()

sales = {
    1: {"item": "Computer", "price": 2000.00},
    2: {"item": "Mouse", "price": 100.00},
    3: {"item": "Keyboard", "price": 200.00},
    4: {"item": "Monitor", "price": 1000.00},
    5: {"item": "Webcam", "price": 300.00},
}

@app.get("/")
def get_health():
    return {"Total sales": len(sales)}

@app.get("/sales/{sale_id}")
def get_sale(sale_id: int):
    if sale_id not in sales:
        return {"error": "Sale not found"}
    return sales[sale_id]

@app.post("/sales/{sale_id}")
def create_sale(sale_id: int, item: str, price: float):
    if sale_id not in sales:
        return {"error": "Sale not found"}
    sales[sale_id] = {"item": item, "price": price}
    return sales[sale_id]

@app.put("/sales/{sale_id}")
def update_sale(sale_id: int, item: str, price: float):
    if sale_id not in sales:
        return {"error": "Sale not found"}
    sales[sale_id] = {"item": item, "price": price}
    return sales[sale_id]

@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: int):
    if sale_id not in sales:
        return {"error": "Sale not found"}
    del sales[sale_id]
    return {"message": "Sale successfully removed"}