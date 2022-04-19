import random
import string
from typing import Iterable, Optional


def generate_password(
    chars: int, punctuation: bool, invalid_chars: Optional[Iterable] = None
) -> str:
    """Make a random string of any length.

    Parameters
    ----------
    chars : int
        Number of characters desired in the output.
    punctuation : bool
        Whether or not to include punctuation characters.
    invalid_chars : Optional[Iterable], optional
        An iterable of characters that should not appear in the result. By default ``None``,
        in which case no extra characters are excluded.

    Returns
    -------
    str
        A random string that can be used as a password.
    """
    # Define character set to use
    valid_chars = string.ascii_letters + string.digits

    # Add punctuation, if desired
    if punctuation:
        valid_chars += string.punctuation

    # If invalid characters are specified, remove those characters
    if invalid_chars is not None:
        for invalid_char in invalid_chars:
            valid_chars = valid_chars.replace(invalid_char, "")

    # Randomly choose from the valid character set and turn into a single str
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
