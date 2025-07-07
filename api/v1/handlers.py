from fastapi import HTTPException

from api.v1.functions import generate_password


async def generate_password_handler(
    length: int,
    use_lowercase: bool = True,
    use_uppercase: bool = False,
    use_digits: bool = False,
    use_special: bool = False
):
    """Password generator handler wih validation."""
    if length < 1 or length > 100:
        raise HTTPException(
            status_code=400,
            detail="Length must be between 1 and 100"
        )
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

    return {
        "password": password
    }
