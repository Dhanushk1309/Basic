from fastapi import FastAPI
from models import product
from database import session
app=FastAPI()
@app.get("/")
def greet():
    return "Welcome to FastAPI"

products = [
    product(id=1, name="laptop", description="A good condition laptop", price=10009.00, quantity=9),
    product(id=2, name="phone", description="A good condition phone", price=599.99, quantity=10),
    product(id=3, name="tablet", description="A good condition tablet", price=399.99, quantity=8),
    product(id=4, name="desktop", description="A good condition desktop", price=20000.00, quantity=5),
    product(id=5, name="airpods", description="A good condition airpods", price=2100.11, quantity=19),
]
@app.get("/products")
def all_products():
    db=session      #db connection
    
    return  products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id==id:
            return product
    return "Product Not found"

@app.post("/product")
def add_product(product:product):
    products.append(product)
    return product 

@app.put("/product")
def update_product(id: int,product:product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product added Succesfully"
    return "No product Found"
            
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id ==id:
            del products[i]
            return "Product Deleted"
    return "Product not found"
