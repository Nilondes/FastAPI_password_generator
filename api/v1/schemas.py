from pydantic import BaseModel, Field


class PasswordGenerateRequest(BaseModel):
    length: int = Field(
        default=8,
        ge=8,
        le=100,
        description="Password strength (8 - 100 symbols)"
    )
    use_lowercase: bool = Field(
        default=False,
        description="Use lowercase (a-z)"
    )
    use_uppercase: bool = Field(
        default=False,
        description="Use uppercase (A-Z)"
    )
    use_digits: bool = Field(
        default=False,
        description="Use digits (0-9)"
    )
    use_special: bool = Field(
        default=False,
        description="Use special characters (!@#$%^&* etc.)"
    )


class PasswordGenerateResponse(BaseModel):
    password: str = Field(description="Generated password")


class PasswordCheckRequest(BaseModel):
    password: str = Field(
        min_length=8,
        max_length=100,
        description="Password for strength evaluation"
    )

class PasswordCheckResponse(BaseModel):
    entropy: float = Field(description="Password entropy in bites")
    strength: str = Field(description="Strength evaluation")
