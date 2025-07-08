from fastapi import HTTPException

from api.v1.functions import generate_password, calculate_entropy, get_strength
from api.v1.schemas import PasswordGenerateResponse, PasswordCheckResponse


async def generate_password_handler(
    length: int,
    use_lowercase: bool = False,
    use_uppercase: bool = False,
    use_digits: bool = False,
    use_special: bool = False
) -> PasswordGenerateResponse:
    """Password generator handler wih validation."""
    if not any([use_lowercase, use_uppercase, use_digits, use_special]):
        raise HTTPException(
            status_code=400,
            detail="At least one parameter must be enabled"
        )

    password = generate_password(
        length=length,
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_special=use_special
    )

    return PasswordGenerateResponse(password=password)


async def check_password_handler(password: str) -> PasswordCheckResponse:
    """Password strength evaluation handler."""
    if len(password) > 100:
        raise HTTPException(
            status_code=400,
            detail="Password exceeds maximum length (100)"
        )
    if not password:
        raise HTTPException(
            status_code=400,
            detail="Password cannot be empty"
        )

    entropy = calculate_entropy(password)
    return PasswordCheckResponse(
        entropy=round(entropy, 2),
        strength=get_strength(entropy)
    )
