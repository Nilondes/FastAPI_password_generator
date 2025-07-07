import math
import random


LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
FULL_ALPHABET = LOWERCASE + UPPERCASE + DIGITS + SPECIAL


def generate_password(
        length: int,
        use_lowercase: bool,
        use_uppercase: bool,
        use_digits: bool,
        use_special: bool
) -> str:
    """Generating password by given parameters."""
    alphabet = ""
    if use_lowercase:
        alphabet += LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL

    return ''.join(random.choices(alphabet, k=length))
