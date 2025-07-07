from fastapi import APIRouter, Query

from .handlers import generate_password_handler


router = APIRouter()


@router.get("")
async def generate_password(
    length: int = Query(ge=8, le=100),
    use_lowercase: bool = Query(False),
    use_uppercase: bool = Query(False),
    use_digits: bool = Query(False),
    use_special: bool = Query(False)
):
    """Endpoint for password generator."""
    return await generate_password_handler(
        length=length,
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_special=use_special
    )
