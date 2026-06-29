from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import products, sales, auth

app = FastAPI(title="POS System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["Productos"])
app.include_router(sales.router, prefix="/sales", tags=["Ventas"])
app.include_router(auth.router, prefix="/auth", tags=["Autenticacion"])

@app.get("/")
def root():
    return {"message": "POS System API corriendo"}