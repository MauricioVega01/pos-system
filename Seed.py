import requests

productos = [
    { "name": "Italiana", "description": "Vienesas", "price": 2500, "stock": 30 },
    { "name": "Dinamica", "description": "Vienesas", "price": 2500, "stock": 30 },
    { "name": "Completo", "description": "Vienesas", "price": 2500, "stock": 30 },
    { "name": "Vienesa con Queso", "description": "Vienesas", "price": 2500, "stock": 30 },
    { "name": "Churrasco", "description": "Churrascos", "price": 4500, "stock": 20 },
    { "name": "Pizza Personal", "description": "Pizza", "price": 3500, "stock": 15 },
    { "name": "Empanada de Pino", "description": "Empanadas", "price": 1800, "stock": 25 },
    { "name": "Papas Fritas", "description": "Papas fritas", "price": 2000, "stock": 40 },
    { "name": "Bebida", "description": "Bebestibles", "price": 1200, "stock": 50 },
    { "name": "Agua", "description": "Bebestibles", "price": 800, "stock": 50 },
    { "name": "Energetica", "description": "Bebestibles", "price": 2200, "stock": 20 },
]

for p in productos:
    res = requests.post("http://127.0.0.1:8000/products/", json=p)
    print(f"{p['name']}: {res.json()}")