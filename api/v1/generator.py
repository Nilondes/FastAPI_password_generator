from fastapi import APIRouter


from api.v1.handlers import get_password


router = APIRouter()


@router.get("")
async def get_password():
        pass
