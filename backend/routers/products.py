from fastapi import APIRouter, HTTPException
from bson import ObjectId
from backend.database import products_collection
from backend.models.product import Product, ProductUpdate

router = APIRouter()

def parse_id(product):
    product["_id"] = str(product["_id"])
    return product

@router.get("/")
def get_products():
    products = list(products_collection.find())
    return [parse_id(p) for p in products]

@router.post("/")
def create_product(product: Product):
    result = products_collection.insert_one(product.model_dump())
    return {"id": str(result.inserted_id), "message": "Producto creado"}

@router.put("/{product_id}")
def update_product(product_id: str, product: ProductUpdate):
    result = products_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product.model_dump(exclude_none=True)}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto actualizado"}

@router.delete("/{product_id}")
def delete_product(product_id: str):
    result = products_collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}