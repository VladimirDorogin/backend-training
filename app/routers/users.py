from  fastapi import APIRouter

router = APIRouter(prefix='/users', tags=["Users"])

@router.get('/ping')
def user_ping():
    return {"ping": "pong"}