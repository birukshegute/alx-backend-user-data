#!/usr/bin/env python3
"""
Encrypts password and validates the provided password with hashed one.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns an encrypted password
    """
    psw = password.encode()
    return bcrypt.hashpw(psw, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates the provided password
    """
    match = False
    psw = password.encode()
    if bcrypt.checkpw(psw, hashed_password):
        match = True
    return match
