from fastapi import APIRouter, HTTPException
from backend.database import db
from backend.models.user import UserRegister, UserLogin
from backend.auth import hashear_password, verificar_password, crear_token

router = APIRouter()

users_collection = db["users"]

@router.post("/register")
def register(user: UserRegister):
    existe = users_collection.find_one({"username": user.username})
    if existe:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    users_collection.insert_one({
        "username": user.username,
        "password": hashear_password(user.password)
    })
    return {"message": "Usuario creado correctamente"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"username": user.username})
    if not db_user or not verificar_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = crear_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}