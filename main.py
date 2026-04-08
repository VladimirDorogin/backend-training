from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
@app.get("/")
def read_root():
    return {"message": "Hi! This is training proj"}

@app.get("/health")
def health_check():
    return {"status": "ok"}