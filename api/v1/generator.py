from fastapi import APIRouter, Depends

from .handlers import generate_password_handler, check_password_handler

from .schemas import (
    PasswordGenerateRequest,
    PasswordGenerateResponse,
    PasswordCheckRequest,
    PasswordCheckResponse
)

router = APIRouter()


@router.get("", response_model=PasswordGenerateResponse)
def generate_password(params: PasswordGenerateRequest = Depends()):
    """Endpoint for password generator."""
    return generate_password_handler(
        length=params.length,
        use_lowercase=params.use_lowercase,
        use_uppercase=params.use_uppercase,
        use_digits=params.use_digits,
        use_special=params.use_special
    )


@router.get("/check",  response_model=PasswordCheckResponse)
def check_password(params: PasswordCheckRequest = Depends()):
    return check_password_handler(params.password)
