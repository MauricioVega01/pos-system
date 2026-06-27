from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel
from typing import List
from backend.database import products_collection, sales_collection

router = APIRouter()

class SaleItem(BaseModel):
    product_id: str
    quantity: int

class Sale(BaseModel):
    items: List[SaleItem]

def parse_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/")
def create_sale(sale: Sale):
    total = 0
    items_detail = []

    for item in sale.items:
        product = products_collection.find_one({"_id": ObjectId(item.product_id)})
        if not product:
            raise HTTPException(status_code=404, detail=f"Producto {item.product_id} no encontrado")
        if product["stock"] < item.quantity:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para {product['name']}")
        
        subtotal = product["price"] * item.quantity
        total += subtotal
        items_detail.append({
            "product_id": item.product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": item.quantity,
            "subtotal": subtotal
        })

        products_collection.update_one(
            {"_id": ObjectId(item.product_id)},
            {"$inc": {"stock": -item.quantity}}
        )

    sale_doc = {
        "items": items_detail,
        "total": total,
        "date": datetime.now()
    }

    result = sales_collection.insert_one(sale_doc)
    return {"id": str(result.inserted_id), "total": total, "message": "Venta registrada"}

@router.get("/")
def get_sales():
    sales = list(sales_collection.find())
    return [parse_id(s) for s in sales]