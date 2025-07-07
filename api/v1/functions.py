import math
import random
import string


LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def generate_password(
        length: int,
        use_lowercase: bool,
        use_uppercase: bool,
        use_digits: bool,
        use_special: bool
) -> str:
    """Generating password by given parameters."""
    alphabet = ""
    password = []
    if use_lowercase:
        alphabet += LOWERCASE
        password.append(random.choice(LOWERCASE))
    if use_uppercase:
        alphabet += UPPERCASE
        password.append(random.choice(UPPERCASE))
    if use_digits:
        alphabet += DIGITS
        password.append(random.choice(DIGITS))
    if use_special:
        alphabet += SPECIAL
        password.append(random.choice(SPECIAL))

    remaining = length - len(password)
    password += random.choices(alphabet, k=remaining)
    random.shuffle(password)
    return ''.join(password)


def calculate_entropy(password: str) -> float:
    """Password Entropy calculation."""
    categories = set()
    charsets = {
        "lower": LOWERCASE,
        "upper": UPPERCASE,
        "digit": DIGITS,
        "special": SPECIAL
    }

    for char in password:
        for cat, charset in charsets.items():
            if char in charset:
                categories.add(cat)
                break

    n = sum(len(charsets[cat]) for cat in categories)
    return len(password) * math.log2(n) if n > 0 else 0.0
