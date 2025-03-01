from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/")
def read_root():
    return {"message": "Welcome to the New Rose Society API!"}